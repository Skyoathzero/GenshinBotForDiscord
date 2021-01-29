import discord
from discord.ext import commands
import logging
from pathlib import Path
import json
from discord.embeds import Embed
import Scrapeweb

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

#Test Command

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
    await bot.logout()


#Scrape web command
@bot.command(name = 'search',aliases = ['s','srch'])
async def search(ctx,*,isian):
    Scrapeweb.Scrape(isian)
    INFO = discord.Embed(title="Here are your search results",
                        description="Please pick the number of your search result that you want to access.\n\n**Number Of Result** : {}".format(Scrapeweb.NO_OF_RESULT),
                        color=0x70d4ff)
    INFO.set_author(name="Paimon",icon_url = "https://upload-os-bbs.mihoyo.com/upload/2020/06/03/6409544/94d2302c0fd450181a6c63d2dfa09687_8638738802068195592.jpg?x-oss-process=image/resize,s_740/quality,q_80/auto-orient,0/interlace,1/format,jpg")
    INFO1 = discord.Embed(title="|| ------------------ ||",url=Scrapeweb.INFO["link1"], description=Scrapeweb.INFO["card_info1"], color=0x70d4ff)
    INFO1.set_author(name="Search Result 1")
    INFO1.set_thumbnail(url=Scrapeweb.INFO["image1"])
    INFO2 = discord.Embed(title="|| ------------------ ||",url=Scrapeweb.INFO["link2"], description=Scrapeweb.INFO["card_info2"], color=0x70d4ff)
    INFO2.set_author(name="Search Result 2")
    INFO2.set_thumbnail(url=Scrapeweb.INFO["image2"])
    INFO3 = discord.Embed(title="|| ------------------ ||",url=Scrapeweb.INFO["link3"], description=Scrapeweb.INFO["card_info3"],color=0x70d4ff)
    INFO3.set_author(name="Search Result 3")
    INFO3.set_thumbnail(url=Scrapeweb.INFO["image3"])
    INFO4 = discord.Embed(title="|| ------------------ ||",url=Scrapeweb.INFO["link4"], description=Scrapeweb.INFO["card_info4"], color=0x70d4ff)
    INFO4.set_author(name="Search Result 4")
    INFO4.set_thumbnail(url=Scrapeweb.INFO["image4"])
    await ctx.send(embed=INFO)
    if Scrapeweb.INFO["card_info1"] != "":
        await ctx.send(embed=INFO1)
        if Scrapeweb.INFO["card_info2"] != "":
            await ctx.send(embed=INFO2)
            if Scrapeweb.INFO["card_info3"] != "":
                await ctx.send(embed=INFO3)
                if Scrapeweb.INFO["card_info4"] != "":
                    await ctx.send(embed=INFO4)
    else: await ctx.send("Sorry, No Result is Found :<")
    
bot.run("NzYyNTIwODUyMzg2MTUyNDc4.X3qW4g.fKD4mSCJL1dWeIf1lvov2CgVAko")