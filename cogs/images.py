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
    isActiveNow = False
    emptyArray = [0]*100

    minTime = 30
    maxTime = 180

    topCardId = ''
    topMoneyId = ''

    currentCard = card.Card("","",-1,-1)

    def __init__(self, bot):
        # Guardar en la base de datos el top de los dos
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if Images.isActive or message.author == self.bot.user:
            return

        timer = random.randint(Images.minTime, Images.maxTime)
        Images.isActive = True
        await asyncio.sleep(timer)
        Images.isActiveNow = True
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
        elif 101 <= indiceRareza <= 102:
            name, link, ID, rareza = card.getRandomCard()
            while rareza != 6:
                name, link, ID, rareza = card.getRandomCard()
            color = 0x000000

        print(f"{ID} - {name}: {link} ")

        Images.currentCard = card.Card(name,link,ID,rareza)
        rar = self.getRareza(rareza)
        await self.print_card(name, link, color, rar)


        # Give roles
        topUser = await self.bot.pg_con.fetch("SELECT * FROM users ORDER BY money DESC LIMIT 1")

        member = None
        for users in topUser:
            member = users['user_id']
            break

        if member == Images.topMoneyId:
            pass
        else:

            guild = self.bot.get_guild(TOKENS.SERVER_ID)  # Server ID
            user = guild.get_member(int(member))


            moneyRole = discord.utils.get(guild.roles, name="Millonario🤑")

            print(f"Old: {Images.topMoneyId}")

            if Images.topMoneyId != '':

                oldUser = guild.get_member(int(Images.topMoneyId))
                await oldUser.remove_roles(moneyRole)

            await user.add_roles(moneyRole)

            Images.topMoneyId = user.id

        topUser = await self.bot.pg_con.fetch("SELECT * FROM users ORDER BY card_count DESC LIMIT 1")

        member = None
        for users in topUser:
            member = users['user_id']
            break

        if member == Images.topCardId:
            pass
        else:

            guild = self.bot.get_guild(TOKENS.SERVER_ID)  # Server ID
            user = guild.get_member(int(member))

            cardRole = discord.utils.get(guild.roles, name="Joker🃏")

            if Images.topCardId != '':
                oldUser = guild.get_member(int(Images.topCardId))
                await oldUser.remove_roles(cardRole)

            Images.topCardId = user.id
            await user.add_roles(cardRole)



    '''
    @commands.command()
    async def set_timer(self, ctx, minn, maxx):
        Images.minTime = minn
        Images.maxTime = maxx
    '''

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
    async def cards(self, ctx, member: discord.Member = None):

        if member is not None:
            user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(member.id))
            cardsArray = user['cards']
            print(cardsArray)
            embedString = ""
            i = 1
            for cardIn in cardsArray:
                if cardIn is None:
                    await ctx.send("Carta corrupta encontrada, arreglando...")
                    await self.bot.pg_con.fetch("UPDATE users VALUES cards[$1] = $2 WHERE user_id = $3 ", i-1, 0, str(ctx.message.author.id))
                    await ctx.send("Arreglado. La cueNta de la carta tuvo que ser reseteada a `0`")
                    continue
                if cardIn != 0:
                    rareza = self.getRareza(card.cards[i - 1].rareza)
                    embedString += f"ID:`{i}` - `{card.cards[i - 1].name}` | Count: `{cardIn}` | `{rareza}`\n"
                i += 1

            embed = discord.Embed(title="Cartas de {}".format(member.display_name), description=embedString).set_thumbnail(
                url=member.avatar_url)

            channel = self.bot.get_channel(Images.channelID)
            await channel.send(embed=embed)

        else:
            user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))
            cardsArray = user['cards']
            print(cardsArray)
            embedString = ""
            i = 1
            for cardIn in cardsArray:
                if cardIn != 0:
                    rareza = self.getRareza(card.cards[i-1].rareza)
                    embedString += f"ID:`{i}` - `{card.cards[i-1].name}` | `{cardIn}` | `{rareza}`\n"
                i += 1

            embed = discord.Embed(title="Cartas de {}".format(ctx.author), description=embedString).set_thumbnail(url=ctx.author.avatar_url)

            channel = self.bot.get_channel(Images.channelID)
            await channel.send(embed=embed)

    def getRareza(self, index):
        if index == 6:
            return "ÃÒœŋ±ĶŅŰł"
        elif index == 5:
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

        if not Images.isActiveNow:
            channel = self.bot.get_channel(Images.channelID)
            toDelete = await channel.send(embed=discord.Embed(title="Pero si no hay nada chaval..."))
            # await ctx.message.delete()
            # await asyncio.sleep(3)
            # await toDelete.delete()
        else:
            Images.isActive = False
            Images.isActiveNow = False
            user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))

            if not user:
                await self.bot.pg_con.execute(
                    "INSERT INTO users (user_id, cards, card_count, money, user_name, power) VALUES ($1, $2, $3, $4, $5, $6)",
                    str(ctx.author.id), Images.emptyArray, 0, 0, str(ctx.message.author), Images.emptyArray)

            user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))
            await self.bot.pg_con.execute("UPDATE users SET card_count = $1 WHERE user_id = $2", user['card_count'] + 1, str(
                ctx.message.author.id))

            print(f"Get: {Images.currentCard.id} {user['cards'][Images.currentCard.id]} {ctx.message.author.id}")
            print(type(Images.currentCard.id), type(user['cards'][Images.currentCard.id] + 1), type(str(ctx.message.author.id)))
            await self.bot.pg_con.execute("UPDATE users SET cards[$1] = $2 WHERE user_id = $3", Images.currentCard.id,
                                          user['cards'][Images.currentCard.id] + 1, str(ctx.message.author.id)) # Updates the array

            color = 0x000000
            if Images.currentCard.rareza == 5:
                color = 0xF4D03F
            elif Images.currentCard.rareza == 4:
                color = 0x7D3C98
            elif Images.currentCard.rareza == 3:
                color = 0x3498DB
            elif Images.currentCard.rareza == 2:
                color = 0x229954
            elif Images.currentCard.rareza == 1:
                color = 0xF0F3F4
            elif Images.currentCard.rareza == 6:
                color = 0x000000


            if Images.currentCard.rareza == 6:
                newEmbed = discord.Embed(title="ĜĹŘðőĪŔňÚ·Ūġūõĵ¥",
                                         description="¢Æ¦ÝŵÿŶ¿ùŝÈıāųĽß±ď³Ňţ¾ĿÊ¹ĴÅŞĪűřĲóůÍĦ°ĚàÐ¸ÖŖĥńŲ×ĊČŊ").set_thumbnail(url="https://pm1.narvii.com/6783/3e8f52fbd11a05b249376f73307a9530eb7e2f9fv2_hq.jpg")
                await Images.savedMessage.edit(embed=newEmbed)
                # await ctx.message.delete()
                return

            newEmbed = discord.Embed(title="Nahhhh, el {} acaba de atrapar un `{}` de rareza `{}`.".format(
                ctx.message.author, Images.currentCard.name, self.getRareza(Images.currentCard.rareza)),
                description="Muy gay.",
                color=color).set_thumbnail(url=Images.currentCard.link)
            await Images.savedMessage.edit(embed=newEmbed)
            # await ctx.message.delete()

    @commands.command()
    async def info(self, ctx, _card_id):
        card_id = int(_card_id)
        info_card = card.cards[card_id - 1]

        color = 1
        if info_card.rareza == 5:
            color = 0xF4D03F
        elif info_card.rareza == 4:
            color = 0x7D3C98
        elif info_card.rareza == 3:
            color = 0x3498DB
        elif info_card.rareza == 2:
            color = 0x229954
        elif info_card.rareza == 1:
            color = 0xF0F3F4

        rar = self.getRareza(info_card.rareza)
        descriptionString = "Rareza: `{}` ".format(rar)
        embedVar = discord.Embed(title="{}".format(info_card.name),
                                 description=descriptionString,
                                 color=color).set_image(url=info_card.link)
        channel = self.bot.get_channel(Images.channelID)
        Images.savedMessage = await channel.send(embed=embedVar)


    async def print_card(self, name, link, color, rareza):
        descriptionString = "Un {} ha aparecido. Atrapalo con `_get`\n".format(name)
        descriptionString += "Rareza: `{}` ".format(rareza)
        embedVar = discord.Embed(title="Aparecio un GAY",
                                 description=descriptionString,
                                 color=color).set_image(url=link)
        channel = self.bot.get_channel(Images.channelID)
        Images.savedMessage = await channel.send(embed=embedVar)



def setup(bot):
    bot.add_cog(Images(bot))