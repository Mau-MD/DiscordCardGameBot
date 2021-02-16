import discord
from discord.ext import commands
import random
import util


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def moneda(self, ctx, _money, _option):
        option = int(_option)
        money = int(_money)

        if option > 1 or option < 0:
            await util.sendMsg(self.bot, "Ingresa una opcion valida, bobo")
            return

        winner = random.randint(0, 1)
        user = await util.getRow(self.bot, str(ctx.message.author.id))
        if option == winner:
            await util.sendMsg(self.bot, "Nicee, ganaste `${}.00`". format(money * 2))
            await util.updateMoney(self.bot, str(ctx.message.author.id), user['money'] + int(money * 2))
        else:
            await util.sendMsg(self.bot, "Babas, acabas de perder `${}.00`".format(money))
            await util.updateMoney(self.bot, str(ctx.message.author.id), user['money'] - int(money))


def setup(bot):
    bot.add_cog(Games(bot))
