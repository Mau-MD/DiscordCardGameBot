import discord
from discord.ext import commands
import asyncio
import random
import card
import TOKENS


channelID = TOKENS.CHANNEL_ID


async def sendMsg(bot, message):
    global channelID
    channel = bot.get_channel(channelID)
    await channel.send(message)


async def sendEmbed(bot, embed):
    global channelID
    channel = bot.get_channel(channelID)
    await channel.send(embed=embed)


async def getRow(bot, user_id):
    return await bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", user_id)


async def updateMoney(bot, user_id, value):
    await bot.pg_con.execute("UPDATE users SET money = $1 WHERE user_id = $2", value, user_id)


async def updateCard(bot, user_id, value):
    await bot.pg_con.execute("UPDATE users SET card_count = $1 WHERE user_id = $2", value, user_id)


async def updateArray(bot, user_id, index, value):
    print(type(index), type(value), type(user_id))
    await bot.pg_con.execute("UPDATE users SET cards[$1] = $2 WHERE user_id = $3", index + 1, value, user_id)  # Updates the ar
    user = await bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", user_id)
    print(user['cards'][index])
