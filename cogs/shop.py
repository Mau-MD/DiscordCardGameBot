import discord
from discord.ext import commands
from dpymenus import Page, PaginatedMenu
import ShopItems
import util


class Shop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx):
        contentSize = len(ShopItems.items)

        newPage = None
        pageNumber = 1
        pageArrays = []
        print(1)

        newPage = Page(title=f"Pagina {pageNumber}", description="🤑🤑🤑")
        for i in range(1, contentSize+1):
            newPage.add_field(name=ShopItems.items[i-1].item, value=f"{ShopItems.items[i-1].description} ---"
                                                                    f" `${ShopItems.items[i-1].price:,d}`")
            print(newPage)
            if i % 10 == 0:
                pageArrays.append(newPage)
                pageNumber += 1
                print(newPage)
                newPage = Page(title=f"Pagina {pageNumber}", description="🤑🤑🤑")

        pageArrays.append(newPage)
        menu = PaginatedMenu(ctx)
        menu.add_pages(pageArrays)
        await menu.open()

    @commands.command()
    async def buy(self, ctx, _item):

        contentSize = len(ShopItems.items)
        item = str(_item)
        item = item.lower()

        user = await util.getRow(self.bot, str(ctx.message.author.id))

        for i in range(0, contentSize):
            if item == ShopItems.items[i].item.lower(): # En este index del array tengo que sumarle
                if user['money'] < ShopItems.items[i].price:
                    await util.sendMsg(self.bot, "No tienes dinero, pobre 🎸")
                    return

            await util.updateMoney(self.bot, str(ctx.message.author.id), user['money'] - ShopItems.items[i].price)
            await util.updatePower(self.bot, str(ctx.message.author.id), i, user['power'])

            await util.sendMsg(self.bot, f"Acabas de comprar un `{ShopItems.items[i].item}` por `{ShopItems.items[i].price:,d}`")






def setup(bot):
    bot.add_cog(Shop(bot))