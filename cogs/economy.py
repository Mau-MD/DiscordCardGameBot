import random
import asyncio
import asyncpg
import discord
from discord.ext import commands
import TOKENS


class Economy(commands.Cog):
    channelID = TOKENS.CHANNEL_ID

    minMoney = 0
    maxMoney = 10000
    moneyPhrases = ["gano dinero vendiendo animes piratas", "gano dinero trabajando duro",
                    "gano dinero como todo un tiburon"]

    emptyArray = [0] * 20

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Espera {error.retry_after:.2f} segundos, mugre spammer 😡😡😡")

    @commands.command()
    async def min_money(self, val):
        Economy.minMoney = val

    @commands.command()
    async def max_money(self, val):
        Economy.maxMoney = val

    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command(pass_content=True)
    async def work(self, ctx):

        money = random.randint(Economy.minMoney, Economy.maxMoney)
        embed = discord.Embed(title="Ganaste ${}.00!".format(money), description="{} {}".format(ctx.author,
                                                                                                random.choice(
                                                                                                    Economy.moneyPhrases))) \
            .set_thumbnail(url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

        user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))

        if not user:
            await self.bot.pg_con.execute(
                "INSERT INTO users (user_id, cards, card_count, money, user_name) VALUES ($1, $2, $3, $4, $5)",
                str(ctx.author.id), Economy.emptyArray, 0, 0, str(ctx.message.author))

        user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))
        await self.bot.pg_con.execute("UPDATE users SET money = $1 WHERE user_id = $2", user['money'] + money,
                                      str(ctx.message.author.id))

    @commands.cooldown(1, 180, commands.BucketType.user)
    @commands.command(pass_content=True)
    async def rob(self, ctx, member: discord.Member):
        success = random.randint(0, 1)
        if success:
            money = random.randint(0, 10000)
            user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1", str(member.id))

            if not user:
                await ctx.send(embed=discord.Embed(title="Ese we ni existe xd"))
                return

            user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(member.id))

            userMoney = user['money']

            money = min(userMoney, money)

            await self.bot.pg_con.execute("UPDATE users SET money = $1 WHERE user_id = $2", user['money'] - money,
                                          str(member.id))

            user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))

            await self.bot.pg_con.execute("UPDATE users SET money = $1 WHERE user_id = $2", user['money'] + money,
                                          str(ctx.message.author.id))

            await ctx.send(embed=discord.Embed(title=f"ATRACO REALIZADO 😳",
                                               description=f"El {ctx.author} acaba de robarle a {member.display_name} una cantidad espantosa de `${money:,d}` 😱")
                           .set_thumbnail(url=ctx.author.avatar_url))



        else:
            money = random.randint(5000, 15000)
            user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))

            if not user:
                await ctx.send(embed=discord.Embed(title="Ni existes xd"))
                return

            user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))

            userMoney = user['money']

            money = min(userMoney, money)

            await self.bot.pg_con.execute("UPDATE users SET money = $1 WHERE user_id = $2", user['money'] - money,
                                          str(ctx.message.author.id))

            await ctx.send(embed=discord.Embed(title=f"BIEN MENSO JAJA 😳",
                                               description=f"El {ctx.author} acaba de perder una cantidad espantosa de `${money:,d}` por baboso😱")
                           .set_thumbnail(url=ctx.author.avatar_url))

    """
    @commands.command(pass_content=True)
    async def money(self, ctx):

        user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))

        if not user:
            embed = discord.Embed(title="No tienes nada... Mugre pobre")
            await ctx.send(embed=embed)
        else:
            user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))
            embed = discord.Embed(title="Dinero de {}".format(ctx.author), description=f"${user['money']:,d} 🤑🤑🤑")\
                .set_thumbnail(url=ctx.author.avatar_url)

            await ctx.send(embed=embed)
    """

    @commands.command(pass_content=True)
    async def money(self, ctx, member: discord.Member = None):

        if member is not None:
            user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1", str(member.id))

            if not user:
                embed = discord.Embed(title="No existe ese we")
                await ctx.send(embed=embed)
            else:
                user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(member.id))
                embed = discord.Embed(title="Dinero de {}".format(member.display_name),
                                      description=f"${user['money']:,d} 🤑🤑🤑") \
                    .set_thumbnail(url=member.avatar_url)
                await ctx.send(embed=embed)
        else:
            user = await self.bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1", str(ctx.message.author.id))

            if not user:
                embed = discord.Embed(title="No tienes nada... Mugre pobre")
                await ctx.send(embed=embed)
            else:
                user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1",
                                                      str(ctx.message.author.id))
                embed = discord.Embed(title="Dinero de {}".format(ctx.author),
                                      description=f"${user['money']:,d} 🤑🤑🤑") \
                    .set_thumbnail(url=ctx.author.avatar_url)

                await ctx.send(embed=embed)

    @commands.command(pass_content=True)
    async def give(self, ctx, member: discord.Member, *, money=0):
        print("hola")
        user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", str(member.id))
        print(user)
        await self.bot.pg_con.execute("UPDATE users SET money = $1 WHERE user_id = $2", user['money'] + money,
                                      str(member.id))
        print(f"{user['money']} {money}")
        await ctx.send(f"Se agregaron ${money:,d} peñacoins a la cuenta de {member.mention}")

    @commands.command()
    async def mleaderboard(self, ctx):
        top10 = await self.bot.pg_con.fetch("SELECT * FROM users ORDER BY money DESC LIMIT 5")

        embedText = ""
        imgLink = ""

        for i in range(0, len(top10)):
            embedText += str(top10[i]['user_name']) + " --------> " + f" ${top10[i]['money']:,d}" + (
                        len(top10) - i) * '🤑' + "\n"
            if i == 0:
                print(top10[i]['user_id'])
                user = self.bot.get_user(int(top10[i]['user_id']))
                imgLink = user.avatar_url

        embed = discord.Embed(title="Money Leaderboard 🤑", description=embedText).set_thumbnail(url=imgLink)
        channel = self.bot.get_channel(Economy.channelID)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Economy(bot))
