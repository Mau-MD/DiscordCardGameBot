import discord
from discord.ext import commands
import random
from Imgs import card
import asyncio

description = '''hola'''
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='_',
                   description=description,
                   intents=intents)

isActive = False
savedMessage = None
channelID = 807399692303859732
Leaderboard = {}

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('-------')


async def showLeaderboard():
  leaderboardText = ""

  for person, score in Leaderboard.items():
    leaderboardText += ("{} -> {} \n".format(person, score))
  
  channel = bot.get_channel(channelID)
  await channel.send(embed = discord.Embed(title="Leaderboard", description=leaderboardText))




async def get(message):

    global savedMessage
    global isActive

    if isActive == False:
        channel = bot.get_channel(channelID)
        await channel.send(embed = discord.Embed(title="Pero si no hay nada chaval..."))
    else:
        isActive = False

        if not str(message.author) in Leaderboard:
          Leaderboard[str(message.author)] = 1
        else:
          Leaderboard[str(message.author)] += 1

        newEmbed = discord.Embed(title="Nahhhh, el {} me atrapo.".format(
                                message.author),
                                description="Muy gay.",
                                color=0x00ff00)
        await savedMessage.edit(embed = newEmbed)


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


@bot.event
async def on_message(message):
    global isActive

    print("author: {}, bot: {}, isActive{}".format(message.author, bot.user, isActive))

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


bot.run('NzUzMjgwNTgwNzE5ODcwMDQ0.X1j5NQ.TMUs167-m442efTnF8mOhOtNc1Y')
