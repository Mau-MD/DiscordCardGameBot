import discord
from discord.ext import commands
import random
from Imgs import card
import asyncio
import asyncpg
import os

description = '''hola'''
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='_',
                   description=description,
                   intents=intents)
                   
isActive = False
savedMessage = None
channelID = os.getenv('CHANNEL_ID')
Leaderboard = {}

emptyArray = [0]*30

async def create_db_pool():
  bot.pg_con = await asyncpg.create_pool(database="pogUBot", user="admin", password=os.getenv('PASSWORD'))




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('-------')


@bot.event
async def on_message(message):
    global isActive

    # print("author: {}, bot: {}, isActive{}".format(message.author, bot.user,  isActive))

    if message.author == bot.user:
        return

    if "_get" in message.content:
        await get(message)
    elif "_leaderboard" in message.content:
        await showLeaderboard()
    elif isActive == True:
        return
    else:
      await start()


async def get(message):

    global savedMessage
    global isActive

    if isActive == False:
        channel = bot.get_channel(channelID)
        await channel.send(embed = discord.Embed(title="Pero si no hay nada chaval..."))
    else:
        isActive = False

        user = await bot.pg_con.fetch("SELECT * FROM users WHERE user_id = $1", message.author.id)

        if not user:
          await bot.pg_con.execute("INSERT INTO users (user_id, cards, card_count, money) VALUES ($1, $2, $3, $4)", message.author.id, emptyArray, 0, 0)

        user = await bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", message.author.id)
        await bot.pg_con.execute("UPDATE users SET card_count = $1 WHERE user_id = $2", user['card_count'] + 1, message.author.id) # Just updates card count, would be nice to update the specific id card number. TODO



        newEmbed = discord.Embed(title="Nahhhh, el {} me atrapo.".format(
                                message.author),
                                description="Muy gay.",
                                color=0x00ff00)
        await savedMessage.edit(embed = newEmbed)


async def showLeaderboard():
  top5 = await bot.pg_con.fetch("SELECT * FROM users ORDER BY card_count DESC LIMIT 5")
  
  embedText = ""

  for i in range(0,5):
    embedText += str(top5[i]['user_id']) + " --------> " + str(top5[i]['card_count']) + "\n"

  embed = discord.Embed(title="Leaderboard", description=embedText)
  channel = bot.get_channel(channelID)
  await channel.send(embed=embed)

async def start():
    global isActive
    isActive = True

    timeToSleep = random.randint(1, 30)
    await asyncio.sleep(timeToSleep)

    name, link, ID = card.getRandomCard()

    print(name + " " + link)

    await printCard(name, link)


async def printCard(name, link):
    global savedMessage
    embedVar = discord.Embed(title="Aparecio un GAY",
                             description="Un {} ha aparecido. Atrapalo con `_get`".format(name),
                             color=0x00ff00).set_image(url=link)
    channel = bot.get_channel(channelID)
    savedMessage = await channel.send(embed=embedVar)




#bot.loop.run_until_complete(create_db_pool())
bot.run(os.getenv('TOKEN'))
