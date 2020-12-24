import discord
from discord.ext import commands
import logging
from pathlib import Path
import json

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n----")

secret_file = json.load(open(cwd+"/bot_config/token.json"))
bot = commands.Bot(command_prefix="g!")
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(Logged in)
    await bot.change_presence(activity=discord.Game(name=f"use g! to use my command"))




bot.run(secret_file['token'])