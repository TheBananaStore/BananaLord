import random
import aiohttp
import requests
import discord
import requests
from discord import Member
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands import has_permissions
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

client = commands.Bot(command_prefix="bl!")
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('under development'))
    print("BL logged on.")

#meme command, from r/memes subreddit.

@slash.slash(
    name="meme",
    description="Displays a random meme from the r/Memes subreddit!",
    guild_ids=[944368087526944778]
)

async def _meme(ctx:SlashContext):
    embed = discord.Embed(title="", description="A random meme for your eyes.", color = (0xfff700))

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/Memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


#random number between 1 and 100

@slash.slash(
    name="randomnum",
    description="Display a random number between 1 and 100!",
    guild_ids=[944368087526944778]
)

async def _randomnum(ctx:SlashContext):
    embed = discord.Embed(title = "Random Number :thumbsup:", description = (random.randint(1, 101)), color = (0xfff700))
    await ctx.send(embed = embed)

#lock a specified channel (the ability to manage channels is required.)

@slash.slash(
    name="lock",
    description="Lock a specified channel, the ability to manage channels is required.",
    guild_ids=[944368087526944778]
)

@commands.has_permissions(manage_channels=True)
async def lock(ctx:SlashContext, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(':white_check_mark: Channel locked.')

#unlock a specified channel (the ability to manage channels is required.)

@slash.slash(
    name="unlock",
    description="Unlock a specified channel, the ability to manage channels is required.",
    guild_ids=[944368087526944778]
)

@commands.has_permissions(manage_channels=True)
async def lock(ctx:SlashContext, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(':white_check_mark: Channel unlocked.')

client.run('OTUzMDkwMjE5MTgyMjYwMjg1.Yi_gbw.XldkfN5wKln9sOmpSqBd1kzEB5k')