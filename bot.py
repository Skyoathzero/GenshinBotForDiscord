import discord
from discord.ext import commands
import logging
from pathlib import Path
import json

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n----")

secret_file = json.load(open(cwd+"/token.json"))
bot = commands.Bot(command_prefix="g!")
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print("logged in")
    await bot.change_presence(activity=discord.Game(name=f"use g! to use my command"))

@bot.command(name = "hi",aliases =['hello'])
async def _hi(ctx):
    await ctx.send(f"Hi {ctx.author.mention}!")


bot.run(secret_file['token'])