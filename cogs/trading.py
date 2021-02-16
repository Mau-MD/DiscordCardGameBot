from discord.ext import commands
import card
import util


class Trading(commands.Cog):

    auction = False
    currentValue = 0
    cardId = 0
    currentId = ''
    ownerId = ''

    def __init__(self, bot):
        self.bot = bot
        Trading.auction = False

    @commands.command()
    async def sell(self, ctx, card_id):
        print("Executing")
        # Checar si tiene la carta
        user = await util.getRow(self.bot, str(ctx.message.author.id))
        print(user)
        print(user['cards'][int(card_id) - 1])
        if user['cards'][int(card_id) - 1] == 0:
            print("No card")
            await util.sendMsg(self.bot, "No tienes esa carta, noob...")
            return
        else:

            print(card.cards[int(card_id) - 1])
            temp_card = card.cards[int(card_id) - 1]
            rareza = temp_card.rareza


            print(rareza)
            precio = 0
            if rareza == 5:
                precio = 100000
            elif rareza == 4:
                precio = 50000
            elif rareza == 3:
                precio = 20000
            elif rareza == 2:
                precio = 5000
            else:
                precio = 1000

            # Los arreglos inician desde 1 y no desde 0

            index = int(int(card_id) - 1)
            value = int(user['cards'][int(card_id) - 1] - 1)
            user_id = str(ctx.message.author.id)

            # print(f"{int(card_id) - 1}, {user['cards'][int(card_id) - 1] - 1}")
            await util.updateArray(self.bot, user_id, index, value)
            print("first")
            await util.updateCard(self.bot, str(ctx.message.author.id),  user['card_count'] - 1)
            print("second")
            await util.updateMoney(self.bot, str(ctx.message.author.id), user['money'] + precio)
            print("third")

            await util.sendMsg(self.bot, "Genial! Vendiste la carta y ganaste {}".format(precio))

    @commands.command()
    async def auction(self, ctx, _card_id, _initialValue):

        print("Executing")

        if Trading.auction:
            print("Bye")
            return

        Trading.cardId = int(_card_id) - 1
        Trading.currentValue = _initialValue
        Trading.ownerId = str(ctx.message.author.id)

        print(Trading.cardId, Trading.currentValue, Trading.ownerId)

        user = await util.getRow(self.bot, str(ctx.message.author.id))

        if user['cards'][Trading.cardId] == 0:
            await util.sendMsg(self.bot, "No tienes esa carta, noob...")
            return
        else:
            Trading.auction = True
            await util.sendMsg(self.bot, "Inicio la subasta de `{}` por `${}.00`".format(card.cards[Trading.cardId].name, Trading.currentValue))

    @commands.command()
    async def bet(self, ctx, _money):

        if not Trading.auction:
            await util.sendMsg(self.bot, "No hay ninguna subasta activa")
            return

        money = int(_money)

        users = await util.getRow(self.bot, str(ctx.message.author.id))
        print(users['money'], money, Trading.currentValue)

        if int(users['money']) < int(money):
            print("Repobre")
            await util.sendMsg(self.bot, "No tienes suficiente dinero, pobre")
            return
        if int(money) <= int(Trading.currentValue):
            print("Pobre")
            await util.sendMsg(self.bot, "Necesitas apostar mas dinero... Pobre")
            return

        Trading.currentValue = money
        Trading.currentId = str(ctx.message.author.id)

        print(Trading.currentValue)
        await util.sendMsg(self.bot, "Apostaste `${}.00`".format(money))

    @commands.command()
    async def end(self, ctx):

        if Trading.ownerId != str(ctx.message.author.id):
            return

        Trading.auction = False

        owner = await util.getRow(self.bot, str(ctx.message.author.id))
        better = await util.getRow(self.bot, str(Trading.currentId))

        # No se pierde la carta, no se gana dinero

        await util.updateMoney(self.bot, str(ctx.message.author.id), int(owner['money']) + int(Trading.currentValue))
        await util.updateMoney(self.bot, str(Trading.currentId), int(better['money']) - int(Trading.currentValue))

        await util.updateArray(self.bot, str(ctx.message.author.id), int(Trading.cardId), int(owner['cards'][Trading.cardId] - 1))
        await util.updateArray(self.bot, str(Trading.currentId), int(Trading.cardId), int(better['cards'][Trading.cardId] + 1))

        await util.sendMsg(self.bot, "La compra fue hecha por `${}.00` 🤑".format(Trading.currentValue))

    @commands.command()
    async def cancel(self, ctx):
        if Trading.ownerId != str(ctx.message.author.id):
            return
        Trading.auction = False
        await util.sendMsg(self.bot, "Se cancela la subasta :(")


def setup(bot):
    bot.add_cog(Trading(bot))
