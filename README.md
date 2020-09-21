import discord
import asyncio
from discord import Status

from Status import Member_Status
from User import User_Who
from Matchmaking import MM

runtime = 0

client = discord.Client()

@client.event
async def on_member_update(before, after):
    await Member_Status(before, after) ## Complete

@client.event
async def on_message(message):
    await User_Who(message) ##Incomplete
    if await User_Who(message):
        await client.delete_message(message)

async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed:
        global run_time
        await MM() ##Incomplete
        print("Runtime: {}s".format(runtime))
        runtime += 10
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print("------Logged in as------")
    print("        {}".format(client.user.name))
    print("   {}".format(client.user.id))
    print("------------------------")
    
client.loop.create_task(my_background_task())
client.run("NDU0OTQ1NTcyNzI2NzY3NjI3.Df04DA.paEHHr5h1frdHFLsth2THp7FFBs")


    
