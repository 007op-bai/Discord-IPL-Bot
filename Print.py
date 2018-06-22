import discord
import asyncio

async def Print_MSG(message):
    timestamp = str(message.timestamp)
    timestamp = timestamp[:-7]
    timestamp = timestamp[11:]
    print("Channel: {} | {} [{}]: {}".format(message.channel, timestamp, message.author, message.content))
