import discord
from discord.ext import commands
from dpymenus import Page, PaginatedMenu
import util
import ShopItems

class Power(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def powerups(self, ctx, member: discord.Member = None):

        if member is None:

            user = await util.getRow(self.bot, str(ctx.message.author.id))
            powerList = user['power']

            embedText = ""
            for i in range(0, len(powerList)):
                if powerList[i] != 0:
                    embedText += f"`{ShopItems.items[i].item}` | Cantidad: `{powerList[i]}`\n"

            await util.sendEmbed(self.bot, discord.Embed(title=f"Powerups de {ctx.author}",
                                                         description=embedText).set_thumbnail(url=ctx.author.avatar_url))


def setup(bot):
    bot.add_cog(Power(bot))
