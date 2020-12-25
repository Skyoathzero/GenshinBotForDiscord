import discord
from discord.ext import commands
import logging
from pathlib import Path
import json
from discord.embeds import Embed

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n----")

secret_file = json.load(open(cwd+"/token.json"))
bot = commands.Bot(command_prefix="g!",owner_id =256755822690959360)
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print("logged in")
    await bot.change_presence(activity=discord.Game(name=f"use g! to use my command"))

@bot.command(name = "hi",aliases =['hello'])
async def _hi(ctx):
    await ctx.send(f"Hi {ctx.author.mention}!")

@bot.command(name = 'stats',aliases = ['stat'])
async def stats(ctx):
    PythonVer = "Python Version"
    DiscordPyVer = "Discord.Py Version"
    ver1 = discord.__version__
    MemberCounts = "Member Counts"
    ver2 = len(set(bot.get_all_members()))
    embed=discord.Embed(title="Server Stats", url=None, description=None, color=0x3dcfff)
    embed.add_field(name=MemberCounts, value=ver2, inline=False)
    embed.add_field(name=PythonVer, value="3.8.3", inline=False)
    embed.add_field(name=DiscordPyVer, value=ver1, inline=False)
    embed.set_footer(text="created by lonelyweeb#2101")
    await ctx.send(embed=embed)

@bot.command(aliases = ["shindeiru","death","oof"])
@commands.is_owner()
async def logout(ctx):
    embed=discord.Embed(title="Commited Disconnect ", description="_Change tha world my final message_", color=0x3dcfff)
    embed.set_footer(text="created by lonelyweeb#2101")
    await ctx.send(embed=embed)

    await bot.logout()
bot.run(secret_file['token'])