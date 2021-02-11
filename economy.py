import random
import asyncio
import asyncpg
import discord
import TOKENS

class economy:

    minMoney = 0
    maxMoney = 0
    moneyPhrases = {"gano dinero vendiendo animes piratas", "gano dinero trabajando duro",
                    "gano dinero como todo un tiburon"}

    def __int__(self, bot):

        self.bot = bot
        # self.bot.loop.create_task(self.)

    async def minmoney(val):
        minMoney = val

    async def maxmoney(val):
        maxMoney = val

    async def work(self, message):
        money = random.randint(economy.minMoney, economy.maxMoney)
        embed = discord.Embed(title="Ganaste ${}.00!".format(money), description="{} + {}".format(message.author,
                                                                                      random.choice(economy.moneyPhrases)))
        channel = self.bot.get_channel(TOKENS.CHANNEL_ID)
        savedMessage = await channel.send(embed=embed)

