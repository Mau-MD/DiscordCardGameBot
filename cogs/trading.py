import discord
from discord.ext import commands
import asyncio
import random
import card
import TOKENS


class Trading(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sell(self, ctx, id):
        # Checar si tiene la carta
        user = await self.bot.pg_con.fetchval("SELECT cards[$1] FROM users WHERE user_id = $2", id-1, str(ctx.message.author.id))
        if user == 0:
            await ctx.send("No tienes esa carta, noob...")
            return
        else:
            precio = 0
            name, link, id, rareza = card.cards[id-1]

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

            await self.bot.pg_con.execute("UPDATE users SET cards[$1] = $2 WHERE user_id = $3", id-1, user-1, str(ctx.message.author.id))
            







def setup(bot):
    bot.add_cog(Trading(bot))