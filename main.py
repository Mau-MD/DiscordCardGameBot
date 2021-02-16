import discord
from discord.ext import commands
import random
import card
import asyncio
import asyncpg
import TOKENS
import os

description = '''hola'''
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='_',
                   description=description,
                   intents=intents)
                   
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

@bot.command()
async def version(ctx):
    global version
    await ctx.send(f"Hola, soy PogU Bot 2 Deluxe, version 6.4")

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
