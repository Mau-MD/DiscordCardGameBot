import discord
from discord.ext import commands
import asyncio
import random
import card
import TOKENS


class Images(commands.Cog):

    savedMessage = None
    channelID = TOKENS.CHANNEL_ID
    isActive = False
    emptyArray = [0]*100

    minTime = 30
    maxTime = 180

    currentCard = card.Card("","",-1,-1)

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if Images.isActive:
            return

        Images.isActive = True
        timer = random.randint(Images.minTime, Images.maxTime)

        await asyncio.sleep(timer)

        # 1 a 5 es exepcional
        # 6 a 15 es leyenda
        # 26 a 40 es raro
        # 41 a 60 es uncomun
        # 61 a 100 es comun

        indiceRareza = random.randint(1, 100)
        print(indiceRareza)
        color = 0xF0F3F4

        if 1 <= indiceRareza <= 5:
            name, link, ID, rareza = card.getRandomCard()
            while rareza != 5:
                name, link, ID, rareza = card.getRandomCard()
            color = 0xF4D03F
        elif 6 <= indiceRareza <= 15:
            name, link, ID, rareza = card.getRandomCard()
            while rareza != 4:
                name, link, ID, rareza = card.getRandomCard()
            color = 0x7D3C98

        elif 16 <= indiceRareza <= 40:
            name, link, ID, rareza = card.getRandomCard()
            while rareza != 3:
                name, link, ID, rareza = card.getRandomCard()
            color = 0x3498DB

        elif 41 <= indiceRareza <= 60:
            name, link, ID, rareza = card.getRandomCard()
            while rareza != 2:
                name, link, ID, rareza = card.getRandomCard()
            color = 0x229954

        elif 61 <= indiceRareza <= 100:
            name, link, ID, rareza = card.getRandomCard()
            while rareza != 1:
                name, link, ID, rareza = card.getRandomCard()
            color = 0xF0F3F4

        print(f"{ID} - {name}: {link} ")

        Images.currentCard = card.Card(name,link,ID,rareza)
        await self.print_card(name, link, color)

    @commands.command()
    async def set_timer(self, ctx, minn, maxx):
        Images.minTime = minn
        Images.maxTime = maxx

    @commands.command()
    async def leaderboard(self, ctx):
        top5 = await self.bot.pg_con.fetch("SELECT * FROM users ORDER BY card_count DESC LIMIT 5")

        embedText = ""
        imgLink = ""

        for i in range(0, len(top5)):
            embedText += str(top5[i]['user_name']) + " --------> " + str(top5[i]['card_count']) + "\n"
            if i == 0:
                print(top5[i]['user_id'])
                user = self.bot.get_user(int(top5[i]['user_id']))
                imgLink = user.avatar_url

        embed = discord.Embed(title="Card Leaderboard 🃏", description=embedText).set_thumbnail(url=imgLink)
        channel = self.bot.get_channel(Images.channelID)
        await channel.send(embed=embed)

    @commands.command()
    async def cards(self, ctx):

        user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))
        cardsArray = user['cards']
        print(cardsArray)
        embedString = ""
        i = 1
        for cardIn in cardsArray:
            if cardIn != 0:
                rareza = self.getRareza(card.cards[i-1].rareza)
                embedString += f"ID:`{i}` - `{card.cards[i-1].name}` - Cantidad: `{cardIn}` - Rareza `{rareza}`\n"
            i += 1

        embed = discord.Embed(title="Cartas de {}".format(ctx.author), description=embedString).set_thumbnail(url=ctx.author.avatar_url)

        channel = self.bot.get_channel(Images.channelID)
        await channel.send(embed=embed)

    def getRareza(self, index):
        if index == 5:
            return "Excepcional"
        elif index == 4:
            return "Leyenda"
        elif index == 3:
            return "Raro"
        elif index == 2:
            return "Uncommon"
        else:
            return "Comun"

    @commands.command()
    async def get(self, ctx):

        if not Images.isActive:
            channel = self.bot.get_channel(Images.channelID)
            await channel.send(embed=discord.Embed(title="Pero si no hay nada chaval..."))
        else:
            Images.isActive = False

            user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))

            if not user:
                await self.bot.pg_con.execute(
                    "INSERT INTO users (user_id, cards, card_count, money, user_name) VALUES ($1, $2, $3, $4, $5)",
                    str(ctx.author.id), Images.emptyArray, 0, 0, str(ctx.message.author))

            user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))
            await self.bot.pg_con.execute("UPDATE users SET card_count = $1 WHERE user_id = $2", user['card_count'] + 1, str(
                ctx.message.author.id))

            print(Images.currentCard.id, user['cards'][Images.currentCard.id], ctx.message.author.id)
            await self.bot.pg_con.execute("UPDATE users SET cards[$1] = $2 WHERE user_id = $3", Images.currentCard.id,
                                          user['cards'][Images.currentCard.id] + 1, str(ctx.message.author.id)) # Updates the array

            newEmbed = discord.Embed(title="Nahhhh, el {} me atrapo.".format(
                ctx.message.author),
                description="Muy gay.",
                color=0x00ff00)
            await Images.savedMessage.edit(embed=newEmbed)

    async def print_card(self, name, link, color):

        embedVar = discord.Embed(title="Aparecio un GAY",
                                 description="Un {} ha aparecido. Atrapalo con `_get`".format(name),
                                 color=color).set_image(url=link)
        channel = self.bot.get_channel(Images.channelID)
        Images.savedMessage = await channel.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Images(bot))