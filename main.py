import random
import os
import json

import config

import aiohttp
import requests
import discord
import youtube_dl
import asyncio
from discord import Member
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands import has_permissions, MissingPermissions
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

client = commands.Bot(command_prefix="bl!")
slash = SlashCommand(client, sync_commands=True)
os.chdir(r'C:\Users\ITdep\Desktop\Coding Projects\Python\Banana Lord Bot')

# Rich presence and status
@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.idle, activity=discord.Game("/botinfo | Banana App Store")
    )
    print("BL logged on.")


# XKCD Command, returns a random xkcd
@slash.slash(
    name="xkcd",
    description="Displays a random xkcd",
    guild_ids=[config.guild_id],
)
async def xkcd(ctx: SlashContext):
    embed = discord.Embed(title="", description="xkcd", color=(0xFFF700))
    url = "https://dynamic.xkcd.com/api-0/jsonp/comic/"
    id = str(random.randint(1, int(requests.get(url).json()["num"])))
    jsonXkcd = requests.get(url + id).json()
    embed = discord.Embed(title="", description=jsonXkcd["alt"], color=(0xFFF700))
    embed.set_image(url=jsonXkcd["img"])
    await ctx.send(embed=embed)


# Meme command, from r/memes subreddit.


@slash.slash(
    name="meme",
    description="Displays a random meme from the r/Memes subreddit!",
    guild_ids=[config.guild_id],
)
async def _meme(ctx: SlashContext):
    embed = discord.Embed(
        title="", description="A random meme for you.", color=(0xFFF700)
    )

    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/Memes/new.json?sort=hot") as r:
            res = await r.json()
            embed.set_image(
                url=res["data"]["children"][random.randint(0, 25)]["data"]["url"]
            )
            await ctx.send(embed=embed)


# Nerdmeme command, from r/programminghumor and r/linuxmeme


@slash.slash(
    name="nerdmeme",
    description="Displays a random meme from a nerdy subreddit",
    guild_ids=[config.guild_id],
)
async def _nerdmeme(ctx: SlashContext):
    embed = discord.Embed(
        title="", description="A random meme for you.", color=(0xFFF700)
    )
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            "https://www.reddit.com/"
            + random.choice(["r/programminghumor", "r/linuxmemes"])
            + "/new.json?sort=hot"
        ) as r:
            res = await r.json()
            embed.set_image(
                url=res["data"]["children"][random.randint(0, 25)]["data"]["url"]
            )
    await ctx.send(embed=embed)


# Random number between 1 and 100


@slash.slash(
    name="randomnum",
    description="Display a random number between 1 and 100!",
    guild_ids=[config.guild_id],
)
async def _randomnum(ctx: SlashContext):
    embed = discord.Embed(
        title="Random Number :thumbsup:",
        description=(random.randint(1, 101)),
        color=(0xFFF700),
    )
    await ctx.send(embed=embed)


# Lock a specified channel (the ability to manage channels is required.)


@slash.slash(
    name="lock",
    description="Lock a specified channel, the ability to manage channels is required.",
    guild_ids=[config.guild_id],
)
@commands.has_permissions(manage_channels=True)
async def lock(ctx: SlashContext, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(":white_check_mark: Channel locked.")


# Unlock a specified channel (the ability to manage channels is required.)


@slash.slash(
    name="unlock",
    description="Unlock a specified channel, the ability to manage channels is required.",
    guild_ids=[config.guild_id],
)
@commands.has_permissions(manage_channels=True)
async def lock(ctx: SlashContext, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(":white_check_mark: Channel unlocked.")


# Dog command, self explanitory
@slash.slash(
    name="doggo",
    description="Display a random dog photo and fact.",
    guild_ids=[config.guild_id],
)
async def doggo(ctx: SlashContext):
    async with aiohttp.ClientSession() as session:
        request = await session.get("https://some-random-api.ml/img/dog")
        dogjson = await request.json()
        request2 = await session.get("https://some-random-api.ml/facts/dog")
        factjson = await request2.json()

        embed = discord.Embed(title="Doggo! :dog:", color=0xFFF700)
        embed.set_image(url=dogjson["link"])
        embed.set_footer(text=factjson["fact"])
        await ctx.send(embed=embed)


# Cat command, self explanitory
@slash.slash(
    name="kitty",
    description="Display a random cat photo and fact.",
    guild_ids=[config.guild_id],
)
async def kitty(ctx: SlashContext):
    async with aiohttp.ClientSession() as session:
        request = await session.get("https://some-random-api.ml/img/cat")
        dogjson = await request.json()
        request2 = await session.get("https://some-random-api.ml/facts/cat")
        factjson = await request2.json()

        embed = discord.Embed(title="Kitty! :cat:", color=0xFFF700)
        embed.set_image(url=dogjson["link"])
        embed.set_footer(text=factjson["fact"])
        await ctx.send(embed=embed)


# Bird command, self explanitory
@slash.slash(
    name="birdy",
    description="Display a random bird photo and fact.",
    guild_ids=[config.guild_id],
)
async def kitty(ctx: SlashContext):
    async with aiohttp.ClientSession() as session:
        request = await session.get("https://some-random-api.ml/img/bird")
        dogjson = await request.json()
        request2 = await session.get("https://some-random-api.ml/facts/bird")
        factjson = await request2.json()

        embed = discord.Embed(title="Birdy! :bird:", color=0xFFF700)
        embed.set_image(url=dogjson["link"])
        embed.set_footer(text=factjson["fact"])
        await ctx.send(embed=embed)


# Coinflip command

determine_flip = [1, 0]


@slash.slash(
    name="coinflip",
    description="Heads or tails, which shall it be?",
    guild_ids=[config.guild_id],
)
async def coinflip(ctx: SlashContext):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(
            title="Coinflip | (Bot Name)",
            color=0xFFF700,
            description=f"{ctx.author.mention} Flipped coin, we got **Heads**! :coin:",
        )
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title="Coinflip | (Bot Name)",
            color=0xFFF700,
            description=f"{ctx.author.mention} Flipped coin, we got **Tails**! :coin:",
        )
        await ctx.send(embed=embed)


# Kick command


@slash.slash(
    name="kick",
    description="Kick a member, the ability to kick members is required.",
    guild_ids=[config.guild_id],
)
@has_permissions(kick_members=True)
async def kick(ctx: SlashContext, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"User {member} was kicked. :white_check_mark:")


@kick.error
async def kick_error(ctx: SlashContext, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permissions to kick people.")


# Ban command


@slash.slash(
    name="ban",
    description="Ban a member, the ability to ban members is required.",
    guild_ids=[config.guild_id],
)
@has_permissions(ban_members=True)
async def ban(ctx: SlashContext, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"User {member} was banned. :white_check_mark:")


@ban.error
async def ban_error(ctx: SlashContext, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permissions to ban people.")


# bot info command
@slash.slash(
    name="botinfo",
    description="Display information about me!",
    guild_ids=[config.guild_id],
)
async def botinfo(ctx: SlashContext):
    embed = discord.Embed(
        title="About Me!", description="Here is some things about me:", color=0xFFF700
    )
    embed.set_author(
        name="Banana Lord 🍌",
        url="https://cdn.discordapp.com/attachments/944368088562929766/953091808240492554/azbear.png",
        icon_url="https://cdn.discordapp.com/attachments/944368088562929766/953091808240492554/azbear.png",
    )
    embed.add_field(
        name="Why?",
        value="I was made to help out in the official Discord server for the Banana Store! But if you would like to add this bot to your own server for free , you can DM Grimet#9620!",
        inline=False,
    )
    embed.add_field(
        name="What is the Banana Store?",
        value="The Banana store is a Linux app store for all major Linux distros!",
        inline=False,
    )
    embed.add_field(
        name="Who made you?", value="The main developer is Grimet#9620", inline=False
    )
    embed.add_field(
        name="Where can I find the app store?",
        value="Here: https://github.com/TheBananaStore/TheBananaStore",
        inline=False,
    )
    embed.add_field(
        name="Does the store have a website?",
        value="Yes, but it is still under development: https://thebananastore.cf",
        inline=False,
    )
    embed.set_footer(
        text="-Banana Lord P.S. Why on earth would you want to know stuff about me?"
    )
    await ctx.send(embed=embed)


# ping pong
@slash.slash(name="ping", description="Pong!", guild_ids=[config.guild_id])
async def ping(ctx: SlashContext):
    embed = discord.Embed(
        title=f":white_check_mark: Pong! Latency: {round(client.latency * 1000)}ms",
        color=0xFFF700,
    )
    await ctx.send(embed=embed)

#server info
@slash.slash(
    name="serverinfo",
    description="Get info about this server!",
    guild_ids=[944368087526944778]
)

async def serverinfo(ctx:SlashContext):
    role_count = len(ctx.guild.roles)

    serverinfoEmbed = discord.Embed(color=0xFFF700)
    serverinfoEmbed.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
    serverinfoEmbed.add_field(name='Member Count', value=ctx.guild.member_count, inline=False)
    serverinfoEmbed.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
    serverinfoEmbed.add_field(name='Highest Role', value=ctx.guild.roles[-2], inline=False)
    serverinfoEmbed.add_field(name='Number of Roles', value=str(role_count), inline=False)

    await ctx.send(embed = serverinfoEmbed)


client.run(config.token)



client.run(config.token)
