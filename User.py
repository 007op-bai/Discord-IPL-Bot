import discord
import asyncio

from Print import Print_MSG
from Queue_join import Queue_Join
from Queue_leave import Queue_Leave
from match_room_1 import M_R_1
from match_room_2 import M_R_2
from match_room_3 import M_R_3
from match_room_4 import M_R_4
from match_room_5 import M_R_5

client = discord.Client()

async def User_Who(message):
    if message.author != client.user:
        await Print_MSG(message) ## Complete
        if str(message.channel) == "queue":
            if message.content.startswith("!join"):
                await Queue_Join() ##Incomplete
            elif message.content.startswith("!leave"):
                await Queue_Leave() ##Incomplete
            else:
                return True
        elif str(message.channel) == "match_room_1":
            await M_R_1() ##Incomplete
        elif str(message.channel) == "match_room_1":
            await M_R_2() ##Incomplete
        elif str(message.channel) == "match_room_1":
            await M_R_3() ##Incomplete
        elif str(message.channel) == "match_room_1":
            await M_R_4() ##Incomplete
        elif str(message.channel) == "match_room_1":
            await M_R_5() ##Incomplete
