TOKEN = "NzY1ODgyOTYyMjMwMjQ3NDI1.X4bSFw.3kFHW66-dDIzosLci_mz3l1BeNk"


import discord
import os
import requests
import json
import random



client = discord.Client()



@client.event
async def on_ready():
    print("{0.user} is up and running bitch!".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    # BOT COMMANDS:


    # Commands for #robotic-peacock-testing
    if message.channel.name == "robotic-peacock-testing":
        if user_message.lower() == "!test":
            print(f"{username} ran !test")
            await message.channel.send(f"stfu {username}")
            return
    

    # Commands for any channel
    if user_message.lower() == "!random":
        randomoutput = int(random.randrange(4))
        print(f"{username} ran !random in {channel} and got response {randomoutput}")
        if randomoutput == 0:
            await message.channel.send(f"hmmm... {random.randrange(100)} seems like a nice number :D")
            return
        if randomoutput == 1:
            await message.channel.send(f"I think {random.randrange(100)} would be fun!")
            return
        if randomoutput == 2:
            await message.channel.send(f"Take my fat {random.randrange(100)}!")
            return
        if randomoutput == 3:
            await message.channel.send(f"idfk what number to give you, go ask <@628105970282790912> or something.")
            return

    if user_message.lower() == "!help":
        print(f"{username} ran !help in {channel}")
        await message.channel.send("Only command is `!help` and `!random` rn...")
        return



client.run(TOKEN)