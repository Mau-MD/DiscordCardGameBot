import discord
from discord.ext import commands
import random
import card
import asyncio
import asyncpg
import TOKENS
import os
import util

description = '''hola'''
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='_',
                   description=description,
                   intents=intents,
                   case_insensitive=True)
                   
isActive = False
savedMessage = None
channelID = TOKENS.CHANNEL_ID
Leaderboard = {}

emptyArray = [0]*30


async def create_db_pool():
  bot.pg_con = await asyncpg.create_pool(database="pogUBot", user="postgres", password=TOKENS.PASSWORD)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('-------')
    await util.sendEmbed(bot, embed=discord.Embed(title="1.0",description="Hola wapos, solo para decirles que ya no sé qué más agregarme, por lo tanto"
                            " mañana será mi actualización final así grande:)\n\n Los quiere, pogUBot").set_thumbnail(url="https://www.dougsartgallery.com/images/ASCII-heart-tattoos-1.gif"))

@bot.command()
async def version(ctx):
    global version
    await ctx.send(f"Hola, soy PogU Bot 0.92 \nNuevo en 0.92: \n`Nuevas Cartas Agregadas`")

for cog in os.listdir(os.path.expanduser('~/Documents/Programming/DiscordCardGameBot/cogs')):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} cannot be loaded: ")
            raise e

bot.loop.run_until_complete(create_db_pool())
bot.run(TOKENS.TOKEN)
