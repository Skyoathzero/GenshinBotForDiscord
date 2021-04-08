import discord
from discord.ext import commands
import logging
from pathlib import Path
import json
from discord.embeds import Embed
# import Scrapeweb
# from Scrapeweb import CHARACTERINFO,CATEGORIES,Scrape,Articlescrape
# from Scrapeweb import INFO as informantion
import asyncio
import os
import sqlite3


cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n----")

secret_file = json.load(open(cwd+"/token.json"))
bot = commands.Bot(command_prefix="g!",owner_id =256755822690959360)
logging.basicConfig(level=logging.INFO)


@bot.event
async def on_ready():
    print("logged in")
    database = sqlite3.connect('main.sqlite')
    cursor = database.cursor()
    cursor.execute("""
    """)
    await bot.change_presence(activity=discord.Game(name=f"use g! to use my command"))

#Test Command
for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')
    else: pass

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'Cogs.{extension}')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'Cogs.{extension}')

@bot.command(name = "hi",aliases =['hello'])
async def _hi(ctx):
    await ctx.send(f"Hi {ctx.author.mention}!")

#STATS Command

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
    embed.add_field(name="Bot Dev",value="<@256755822690959360>")
    embed.set_footer(text="created by lonelyweeb#2101")
    await ctx.send(embed=embed)

#Turn OFF The Bot

@bot.command(aliases = ["shindeiru","death","oof"])
@commands.is_owner()
async def logout(ctx):
    embed=discord.Embed(title="Commited Disconnect ", description="_Change tha world my final message_", color=0x3dcfff)
    embed.set_footer(text="created by lonelyweeb#2101")
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    #Ignore these errors
    ignored = (commands.CommandNotFound, commands.UserInputError)
    if isinstance(error, ignored):
        return
    #Begin error handling
    #Command Timeout 
    if isinstance(error, commands.CommandOnCooldown):
        m, s = divmod(error.retry_after, 60)
        h, m = divmod(m, 60)
        if int(h) is 0 and int(m) is 0:
            await ctx.send(f' You must wait {int(s)} seconds to use this command!')
        elif int(h) is 0 and int(m) is not 0:
            await ctx.send(f' You must wait {int(m)} minutes and {int(s)} seconds to use this command!')
        else:
            await ctx.send(f' You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!')
    #Command Perm Check
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Hey! You lack permission to use this command.")
    raise error


#testing webhook 


#Scrape web command
# @bot.command(name = 'search',aliases = ['s','srch'])
# async def search(ctx,*,isian):
#     Scrapeweb.Scrape(isian)
#     INFO = discord.Embed(title="Here are your search results",
#                         description="Please pick the number of your search result that you want to access.\n\n**Number Of Result** : {}".format(Scrapeweb.NO_OF_RESULT),
#                         color=0x70d4ff)
#     INFO.set_author(name="Paimon",icon_url = "https://upload-os-bbs.mihoyo.com/upload/2020/06/03/6409544/94d2302c0fd450181a6c63d2dfa09687_8638738802068195592.jpg?x-oss-process=image/resize,s_740/quality,q_80/auto-orient,0/interlace,1/format,jpg")
#     INFO1 = discord.Embed(title="|| ------------------ ||",url=Scrapeweb.INFO["link1"], description=Scrapeweb.INFO["card_info1"], color=0x70d4ff)
#     INFO1.set_author(name="Search Result 1")
#     INFO1.set_thumbnail(url=Scrapeweb.INFO["image1"])
#     INFO2 = discord.Embed(title="|| ------------------ ||",url=Scrapeweb.INFO["link2"], description=Scrapeweb.INFO["card_info2"], color=0x70d4ff)
#     INFO2.set_author(name="Search Result 2")
#     INFO2.set_thumbnail(url=Scrapeweb.INFO["image2"])
#     INFO3 = discord.Embed(title="|| ------------------ ||",url=Scrapeweb.INFO["link3"], description=Scrapeweb.INFO["card_info3"],color=0x70d4ff)
#     INFO3.set_author(name="Search Result 3")
#     INFO3.set_thumbnail(url=Scrapeweb.INFO["image3"])
#     INFO4 = discord.Embed(title="|| ------------------ ||",url=Scrapeweb.INFO["link4"], description=Scrapeweb.INFO["card_info4"], color=0x70d4ff)
#     INFO4.set_author(name="Search Result 4")
#     INFO4.set_thumbnail(url=Scrapeweb.INFO["image4"])
#     await ctx.send(embed=INFO)
#     sent = []
#     if Scrapeweb.INFO["card_info1"] != "":
#         await ctx.send(embed=INFO1)
#         sent.append('1')
#         if Scrapeweb.INFO["card_info2"] != "":
#             await ctx.send(embed=INFO2)
#             sent.append('2')
#             if Scrapeweb.INFO["card_info3"] != "":
#                 await ctx.send(embed=INFO3)
#                 sent.append('3')
#                 if Scrapeweb.INFO["card_info4"] != "":
#                     await ctx.send(embed=INFO4)
#                     sent.append('4')
#         # try : 
#         selection = await bot.wait_for(
#         'message',
#         timeout=60,
#         check=lambda message: message.author == ctx.author
#         )
#         print(selection)
#         if selection.content == "1"and selection.content in sent:
#             print("scraping")
#             Articlescrape(informantion["link1"])
#             if CATEGORIES['category'] == 'character':


#                 content = CHARACTERINFO
#                 Nama = content["Name"]
#                 Img = Scrapeweb.INFO["image1"]
#                 tempList = content["General_Info"]
#                 separator = "\n"
#                 generalinfo= separator.join(tempList)
#                 description = content["Description"]
#                 ingameDescription = content["Ingame_description"]
#                 embed=discord.Embed(title="--------General info--------", description=generalinfo)
#                 embed.set_author(name="-----"+Nama+"-----")
#                 embed.set_thumbnail(url=Img)
#                 embed.add_field(name="Description", value=description, inline=False)
#                 embed.add_field(name="Ingame Description", value=ingameDescription, inline=False)
#                 await ctx.send(embed=embed)
#         if selection.content == "2" and selection.content in sent:
#             print("scraping")
#             Articlescrape(informantion["link2"])
#             if CATEGORIES['category'] == 'character':


#                 content = CHARACTERINFO
#                 Nama = content["Name"]
#                 Img = Scrapeweb.INFO["image2"]
#                 tempList = content["General_Info"]
#                 separator = "\n"
#                 generalinfo= separator.join(tempList)
#                 description = content["Description"]
#                 ingameDescription = content["Ingame_description"]
#                 embed=discord.Embed(title="--------General info--------", description=generalinfo)
#                 embed.set_author(name="-----"+Nama+"-----")
#                 embed.set_thumbnail(url=Img)
#                 embed.add_field(name="Description", value=description, inline=False)
#                 embed.add_field(name="Ingame Description", value=ingameDescription, inline=False)
#                 await ctx.send(embed=embed)
#         if selection.content == "3"and selection.content in sent:
#             print("scraping")
#             Articlescrape(informantion["link3"])
#             print()
#             if CATEGORIES['category'] == 'character':

#                 content = CHARACTERINFO
#                 Nama = content["Name"]
#                 Img = Scrapeweb.INFO["image3"]
#                 tempList = content["General_Info"]
#                 separator = "\n"
#                 generalinfo= separator.join(tempList)
#                 description = content["Description"]
#                 ingameDescription = content["Ingame_description"]
#                 embed=discord.Embed(title="--------General info--------", description=generalinfo)
#                 embed.set_author(name="-----"+Nama+"-----")
#                 embed.set_thumbnail(url=Img)
#                 embed.add_field(name="Description", value=description, inline=False)
#                 embed.add_field(name="Ingame Description", value=ingameDescription, inline=False)
#                 await ctx.send(embed=embed)
#             else : await ctx.send("This Category Maybe is unsuported or underdevelopment")
#         if selection.content == "4"and selection.content in sent:
#             print("scraping")
#             Articlescrape(informantion["link4"])
#             if CATEGORIES['category'] == 'character':

#                 content = CHARACTERINFO
#                 Nama = content["Name"]
#                 Img = Scrapeweb.INFO["image4"]
#                 tempList = content["General_Info"]
#                 separator = "\n"
#                 generalinfo= separator.join(tempList)
#                 description = content["Description"]
#                 ingameDescription = content["Ingame_description"]
#                 embed=discord.Embed(title="--------General info--------", description=generalinfo)
#                 embed.set_author(name="-----"+Nama+"-----")
#                 embed.set_thumbnail(url=Img)
#                 embed.add_field(name="Description", value=description, inline=False)
#                 embed.add_field(name="Ingame Description", value=ingameDescription, inline=False)
#                 await ctx.send(embed=embed)
#         # except asyncio.TimeoutError():
#         else : print("failed") 
#     else: await ctx.send("Sorry, No Result is Found :<")
    
bot.run("NzYyNTIwODUyMzg2MTUyNDc4.X3qW4g.fKD4mSCJL1dWeIf1lvov2CgVAko")  