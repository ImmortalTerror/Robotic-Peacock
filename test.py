import discord
import random

client = discord.Client()

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    server = str(message.guild.name)


    if user_message.lower() == "!dm":
        await message.channel.send(f"Sent you a dm {username}")

        randomoutput = int(random.randrange(5))
        print(f"({server}) >> {username} ran !dm in {channel} and got output {randomoutput}")

        if randomoutput == 0:
            await message.author.send("Output 0")
            return
        elif randomoutput == 1:
            await message.author.send("Output 1")
            return
        elif randomoutput == 2:
            await message.author.send("Output 2")
            return
        elif randomoutput == 3:
            await message.author.send("Output 3")
            return
        elif randomoutput == 4:
            await message.author.send("Output 4")
            return
        return


client.run("NzY1ODgyOTYyMjMwMjQ3NDI1.X4bSFw.3kFHW66-dDIzosLci_mz3l1BeNk")

# import discord

# client = discord.Client()

# @client.event
# async def on_message(message):
#     if message.content.lower() == "!dm":
#         await message.author.send("Text")
#         return


# client.run("NzY1ODgyOTYyMjMwMjQ3NDI1.X4bSFw.3kFHW66-dDIzosLci_mz3l1BeNk")