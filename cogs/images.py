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
    emptyArray = [0]*20

    minTime = 1
    maxTime = 60

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if Images.isActive:
            return

        Images.isActive = True
        timer = random.randint(Images.minTime, Images.maxTime)

        await asyncio.sleep(timer)
        name, link, ID = card.getRandomCard()

        print(f"{id} - {name}: {link} ")

        await self.print_card(name, link)

    @commands.command()
    async def set_timer(self, ctx, minn, maxx):
        Images.minTime = minn
        Images.maxTime = maxx


    @commands.command()
    async def leaderboard(self, ctx):
        top5 = await self.bot.pg_con.fetch("SELECT * FROM users ORDER BY card_count DESC LIMIT 5")

        embedText = ""

        for i in range(0, len(top5)):
            embedText += str(top5[i]['user_name']) + " --------> " + str(top5[i]['card_count']) + "\n"

        embed = discord.Embed(title="Leaderboard", description=embedText)
        channel = self.bot.get_channel(Images.channelID)
        await channel.send(embed=embed)

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

            newEmbed = discord.Embed(title="Nahhhh, el {} me atrapo.".format(
                ctx.message.author),
                description="Muy gay.",
                color=0x00ff00)
            await Images.savedMessage.edit(embed=newEmbed)

    async def print_card(self, name, link):

        embedVar = discord.Embed(title="Aparecio un GAY",
                                 description="Un {} ha aparecido. Atrapalo con `_get`".format(name),
                                 color=0x00ff00).set_image(url=link)
        channel = self.bot.get_channel(Images.channelID)
        Images.savedMessage = await channel.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Images(bot))