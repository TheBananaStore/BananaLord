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
  print("BL logged on.")

@slash.slash(
    name="randomnum",
    description="Display a random number between 1 and 100!",
    guild_ids=[944368087526944778]
)

async def _randomnum(ctx:SlashContext):
    embed = discord.Embed(title = "Random Number :thumbsup:", description = (random.randint(1, 101)), color = (0xfff700))
    await ctx.send(embed = embed)

client.run('OTUzMDkwMjE5MTgyMjYwMjg1.Yi_gbw.XldkfN5wKln9sOmpSqBd1kzEB5k')