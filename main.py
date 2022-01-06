# TO DO
# -Math bot (I need to learn how to get the text after a message)
# -Basic moderation
# -Learn discord commands extention (I will probably have to re-write the whole bot)
# -Science cause SquidBoi wants it. I will probably just find some random science fact api
# 
# 
# 
# 


# Gets token from .env
with open('token.env', 'r') as file:
    TOKEN = file.read().rstrip()


import discord
import random
from datetime import datetime



client = discord.Client()



@client.event
async def on_ready():
    print("{0.user} is up and running bitch!".format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    now = datetime.now()
    current_time = now.strftime("%D %H:%M")
    print(f"{current_time} - ({message.guild.name} - {message.channel.name}) {message.author}: {message.content}")


    # BOT COMMANDS:


    # Commands for #robotic-peacock-testing
    if message.channel.name == "robotic-peacock-testing":

        # !test
        if message.content.lower() == "!test":
            now = datetime.now()
            current_time = now.strftime("%D %H:%M")
            print(f"{current_time} - ({message.guild.name}) >> {message.author} ran !test")
            await message.channel.send(f"stfu {message.author}")
            return


    # Commands for any channel

    # !random
    if message.content.lower() == "!random":
        randomoutput = int(random.randrange(7))
        now = datetime.now()
        current_time = now.strftime("%D %H:%M")
        print(f"{current_time} - ({message.guild.name}) >> {message.author} ran !random in {message.channel.name} and got response {randomoutput}")
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
        if randomoutput == 4:
            await message.channel.send(f"Here's a {random.randrange(100)}")
            return
        if randomoutput == 5:
            await message.channel.send(f"Something tells me that you want {random.randrange(100)}...")
            return
        if randomoutput == 6:
            await message.channel.send(f"You seems like the kind of person to want {random.randrange(100)}")
            return


    # !help
    if message.content.lower() == "!help":
        now = datetime.now()
        current_time = now.strftime("%D %H:%M")
        print(f"{current_time} - ({message.guild.name}) >> {message.author} ran !help in {message.channel.name}")
        embed=discord.Embed(title="Robotic Peacock", description="Commands:", color=0x002fa0)
        embed.set_thumbnail(url="https://i.imgur.com/uN7ki7X.png")
        embed.add_field(name="!help", value="Shows you a list of commands.", inline=False)
        embed.add_field(name="!random", value="Gives you a random number from 0-100... Most of the time.", inline=False)
        embed.add_field(name="!flirt", value="You have to be really lonely to use this command.", inline=False)
        embed.set_footer(text="This bot is still in development and has a long way to go")
        await message.channel.send(embed=embed)
        return


    # !flirt
    if message.content.lower() == "!flirt":
        await message.channel.send(f"Send you a dm <@{message.author.id}> :kissing_heart:")

        randomoutput = int(random.randrange(12))
        now = datetime.now()
        current_time = now.strftime("%D %H:%M")
        print(f"{current_time} - ({message.guild.name}) >> {message.author} ran !flirt and got output {randomoutput}")

        if randomoutput == 0:
            await message.author.send("Whats up baby :smirk:")
            return
        elif randomoutput == 1:
            await message.author.send("Sorry but your not my type. No hard feelings :)")
            return
        elif randomoutput == 2:
            await message.author.send("I hope you know CPR, because you just took my breath away :heart_eyes:")
            return
        elif randomoutput == 3:
            await message.author.send("I was wondering if you’re an artist because you were so good at drawing me in.")
            return
        elif randomoutput == 4:
            await message.author.send("If you were a Transformer, you’d be ‘Optimus Fine.’")
            return
        elif randomoutput == 5:
            await message.author.send("Is your name Google? Because you have everything I’m searching for :smiling_imp:")
            return
        elif randomoutput == 6:
            await message.author.send("Are you a time traveler? Because I absolutely see you in my future :timer:")
            return
        elif randomoutput == 7:
            await message.author.send("Hi, I’m Robotic Peacock. Do you remember me? Oh, that’s right—we’ve only met in my dreams :sleeping:")
            return
        elif randomoutput == 8:
            await message.author.send("Your hand looks heavy—can I hold it for you?")
            return
        elif randomoutput == 9:
            await message.author.send("The sparkle in your eyes is so bright, the sun must be jealous.")
            return
        elif randomoutput == 10:
            await message.author.send("no.")
            return
        elif randomoutput == 11:
            await message.author.send("I'm taken... sorry :)")
            return

    return




client.run(TOKEN)
