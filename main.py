# TO DO
# -Start again from scratch


# Gets token from .env
with open("token.env", "r") as file:
    TOKEN = file.read().rstrip()


import discord
import random
from datetime import datetime


client = discord.Client()


def getTime():
    now = datetime.now()
    current_time = now.strftime("%D %H:%M")
    return current_time


@client.event
async def on_ready():
    print("{0.user} is up and running bitch!".format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return
    try:
        print(
            f"{getTime()} - ({message.guild.name} - {message.channel.name}) {message.author}: {message.content}"
        )
    except AttributeError:
        print(f"{getTime()} - (Direct message) {message.author}: {message.content}")
        return

    # BOT COMMANDS:

    # Commands for #robotic-peacock-testing
    if message.channel.name == "robotic-peacock-testing":

        # !test
        if message.content.lower() == "!test":
            print(f"{getTime()} - ({message.guild.name}) >> {message.author} ran !test")
            await message.channel.send(f"stfu {message.author}")
            return

    # Commands for any channel

    # !random
    if message.content.lower() == "!random":

        lines = [
            "You seems like the kind of person to want {num}",
            "Something tells me that you want {num}...",
            "Take my fat {num}!",
            "I think {num} would be fun!",
            "hmmm... {num} seems like a nice number :D",
        ]
        num = random.randint(1, 100)
        line = random.choice(lines)
        print(
            f'{getTime()} - ({message.guild.name}) >> {message.author} ran !random in {message.channel.name} and got response "{line.format(num=num)}"'
        )
        await message.channel.send(line.format(num=num))

    # !help
    if message.content.lower() == "!help":
        print(
            f"{getTime()} - ({message.guild.name}) >> {message.author} ran !help in {message.channel.name}"
        )
        embed = discord.Embed(
            title="Robotic Peacock", description="Commands:", color=0x002FA0
        )
        embed.set_thumbnail(url="https://i.imgur.com/uN7ki7X.png")
        embed.add_field(
            name="!help", value="Shows you a list of commands.", inline=False
        )
        embed.add_field(
            name="!random",
            value="Gives you a random number from 0-100... Most of the time.",
            inline=False,
        )
        embed.add_field(
            name="!flirt",
            value="You have to be really lonely to use this command.",
            inline=False,
        )
        embed.set_footer(
            text="This bot is still in development and has a long way to go"
        )
        await message.channel.send(embed=embed)
        return

    # !flirt
    if message.content.lower() == "!flirt":
        await message.channel.send(
            f"Send you a dm <@{message.author.id}> :kissing_heart:"
        )

        lines = [
            "I'm taken... sorry :)",
            "no.",
            "The sparkle in your eyes is so bright, the sun must be jealous.",
            "Your hand looks heavy—can I hold it for you?",
            "Hi, I’m Robotic Peacock. Do you remember me? Oh, that’s right—we’ve only met in my dreams :sleeping:",
            "Are you a time traveler? Because I absolutely see you in my future :timer:",
            "Is your name Google? Because you have everything I’m searching for :smiling_imp:",
            "If you were a Transformer, you’d be ‘Optimus Fine.’",
            "I was wondering if you’re an artist because you were so good at drawing me in.",
            "I hope you know CPR, because you just took my breath away :heart_eyes:",
            "Sorry but your not my type. No hard feelings :)",
            "Whats up baby :smirk:",
        ]
        line = random.choice(lines)
        print(
            f'{getTime()} - ({message.guild.name}) >> {message.author} ran !flirt in {message.channel.name} and got response "{line}"'
        )

        await message.author.send(line)
        return

    return


client.run(TOKEN)
