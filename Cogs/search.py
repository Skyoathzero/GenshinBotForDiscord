import discord
from discord.ext import commands
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
try:
    from module import Scrapeweb
    from module.Scrapeweb import CHARACTERINFO,CATEGORIES,Scrape,Articlescrape,WEAPONINFO
    from module.Scrapeweb import INFO as informantion
except : pass
class search(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(name = 'search',aliases = ['s','srch'])
    async def search(self,ctx,*,isian):
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
        sent = []
        if Scrapeweb.INFO["card_info1"] != "":
            await ctx.send(embed=INFO1)
            sent.append('1')
            if Scrapeweb.INFO["card_info2"] != "":
                await ctx.send(embed=INFO2)
                sent.append('2')
                if Scrapeweb.INFO["card_info3"] != "":
                    await ctx.send(embed=INFO3)
                    sent.append('3')
                    if Scrapeweb.INFO["card_info4"] != "":
                        await ctx.send(embed=INFO4)
                        sent.append('4')
            try : 
                selection = await self.client.wait_for("message",
                timeout=60,
                check=lambda message: message.author == ctx.author
                )
            except TimeoutError:
                await ctx.send("Message Timeout")
            print(selection)
            if selection.content == "1"and selection.content in sent:
                print("scraping")
                Articlescrape(informantion["link1"])
                if CATEGORIES['category'] == 'character':
                
                    content = CHARACTERINFO
                    Nama = content["Name"]
                    Img = Scrapeweb.INFO["image1"]
                    tempList = content["General_Info"]
                    separator = "\n"
                    generalinfo= separator.join(tempList)
                    description = content["Description"]
                    ingameDescription = content["Ingame_description"]
                    character1=discord.Embed(title="--------General info--------", description=generalinfo)
                    character1.set_author(name="-----"+Nama+"-----")
                    character1.set_thumbnail(url=Img)
                    character1.add_field(name="Description", value=description, inline=False)
                    character1.add_field(name="Ingame Description", value=ingameDescription, inline=False)
                    
                    character2 = discord.Embed(title="--------------------")
                    character2.set_author(name=".-----Talents-----.")
                    keysTalent = list(CHARACTERINFO["Talents"])
                    for key in keysTalent:
                        talentDesc = [i for i in CHARACTERINFO["Talents"][key]]
                        character2.add_field(name=key, value=separator.join(talentDesc), inline=False)

                    character3 = discord.Embed(title="--------------------")
                    character3.set_author(name=".-----Constelations-----.")
                    keysConst = list(CHARACTERINFO["Constelations"])
                    for key in keysConst:
                        constDesc = [i for i in CHARACTERINFO["Constelations"][key]]
                        character3.add_field(name=key, value=separator.join(constDesc), inline=False)
                    EmbedList = [character1,character2,character3]
                    paginator = BotEmbedPaginator(ctx, EmbedList)
                    await paginator.run()
                if CATEGORIES['category'] == 'weapons':
                    Wname       = WEAPONINFO["Name"]
                    Wimg        = WEAPONINFO["Img"]
                    Winfo       = WEAPONINFO["Info"]
                    Wlore       = WEAPONINFO["Lore"]
                    WabilityT   = WEAPONINFO["Ability"][0]
                    WabilityC   = WEAPONINFO["Ability"][1]
                    Weapon1 = discord.Embed(title="---------------",description=Winfo)
                    Weapon1.set_author(name=Wname)
                    Weapon1.add_field(name=WabilityT, value=WabilityC ,inline=False)
                    Weapon1.set_image(url="https://www.gensh.in"+Wimg)
                    Weapon2 =discord.Embed(title="---------------", description=Wlore)
                    Weapon2.set_author(name="Lore")
                    listofembed = [Weapon1,Weapon2]
                    paginator = BotEmbedPaginator(ctx, listofembed)
                    await paginator.run()
                else : await ctx.send("This Category Maybe is unsuported or underdevelopment")
            if selection.content == "2" and selection.content in sent:
                print("scraping")
                Articlescrape(informantion["link2"])
                if CATEGORIES['category'] == 'character':
                    content = CHARACTERINFO
                    Nama = content["Name"]
                    Img = Scrapeweb.INFO["image2"]
                    tempList = content["General_Info"]
                    separator = "\n"
                    generalinfo= separator.join(tempList)
                    description = content["Description"]
                    ingameDescription = content["Ingame_description"]
                    character1=discord.Embed(title="--------General info--------", description=generalinfo)
                    character1.set_author(name="-----"+Nama+"-----")
                    character1.set_thumbnail(url=Img)
                    character1.add_field(name="Description", value=description, inline=False)
                    character1.add_field(name="Ingame Description", value=ingameDescription, inline=False)
                    
                    character2 = discord.Embed(title="--------------------")
                    character2.set_author(name=".-----Talents-----.")
                    keysTalent = list(CHARACTERINFO["Talents"])
                    for key in keysTalent:
                        talentDesc = [i for i in CHARACTERINFO["Talents"][key]]
                        character2.add_field(name=key, value=separator.join(talentDesc), inline=False)

                    character3 = discord.Embed(title="--------------------")
                    character3.set_author(name=".-----Constelations-----.")
                    keysConst = list(CHARACTERINFO["Constelations"])
                    for key in keysConst:
                        constDesc = [i for i in CHARACTERINFO["Constelations"][key]]
                        character3.add_field(name=key, value=separator.join(constDesc), inline=False)
                    EmbedList = [character1,character2,character3]
                    paginator = BotEmbedPaginator(ctx, EmbedList)
                    await paginator.run()
                if CATEGORIES['category'] == 'weapons':
                    Wname       = WEAPONINFO["Name"]
                    Wimg        = WEAPONINFO["Img"]
                    Winfo       = WEAPONINFO["Info"]
                    Wlore       = WEAPONINFO["Lore"]
                    WabilityT   = WEAPONINFO["Ability"][0]
                    WabilityC   = WEAPONINFO["Ability"][1]
                    Weapon1 = discord.Embed(title="---------------",description=Winfo)
                    Weapon1.set_author(name=Wname)
                    Weapon1.add_field(name=WabilityT, value=WabilityC ,inline=False)
                    Weapon1.set_image(url="https://www.gensh.in"+Wimg)
                    Weapon2 =discord.Embed(title="---------------", description=Wlore)
                    Weapon2.set_author(name="Lore")
                    listofembed = [Weapon1,Weapon2]
                    paginator = BotEmbedPaginator(ctx, listofembed)
                    await paginator.run()
                else : await ctx.send("This Category Maybe is unsuported or underdevelopment")
            if selection.content == "3"and selection.content in sent:
                print("scraping")
                Articlescrape(informantion["link3"])
                print()
                if CATEGORIES['category'] == 'character':

                    content = CHARACTERINFO
                    Nama = content["Name"]
                    Img = Scrapeweb.INFO["image3"]
                    tempList = content["General_Info"]
                    separator = "\n"
                    generalinfo= separator.join(tempList)
                    description = content["Description"]
                    ingameDescription = content["Ingame_description"]
                    character1=discord.Embed(title="--------General info--------", description=generalinfo)
                    character1.set_author(name="-----"+Nama+"-----")
                    character1.set_thumbnail(url=Img)
                    character1.add_field(name="Description", value=description, inline=False)
                    character1.add_field(name="Ingame Description", value=ingameDescription, inline=False)
                    
                    character2 = discord.Embed(title="--------------------")
                    character2.set_author(name=".-----Talents-----.")
                    keysTalent = list(CHARACTERINFO["Talents"])
                    for key in keysTalent:
                        talentDesc = [i for i in CHARACTERINFO["Talents"][key]]
                        character2.add_field(name=key, value=separator.join(talentDesc), inline=False)

                    character3 = discord.Embed(title="--------------------")
                    character3.set_author(name=".-----Constelations-----.")
                    keysConst = list(CHARACTERINFO["Constelations"])
                    for key in keysConst:
                        constDesc = [i for i in CHARACTERINFO["Constelations"][key]]
                        character3.add_field(name=key, value=separator.join(constDesc), inline=False)
                    EmbedList = [character1,character2,character3]
                    paginator = BotEmbedPaginator(ctx, EmbedList)
                    await paginator.run()
                if CATEGORIES['category'] == 'weapons':
                    Wname       = WEAPONINFO["Name"]
                    Wimg        = WEAPONINFO["Img"]
                    Winfo       = WEAPONINFO["Info"]
                    Wlore       = WEAPONINFO["Lore"]
                    WabilityT   = WEAPONINFO["Ability"][0]
                    WabilityC   = WEAPONINFO["Ability"][1]
                    Weapon1 = discord.Embed(title="---------------",description=Winfo)
                    Weapon1.set_author(name=Wname)
                    Weapon1.add_field(name=WabilityT, value=WabilityC ,inline=False)
                    Weapon1.set_image(url="https://www.gensh.in"+Wimg)
                    Weapon2 =discord.Embed(title="---------------", description=Wlore)
                    Weapon2.set_author(name="Lore")
                    listofembed = [Weapon1,Weapon2]
                    paginator = BotEmbedPaginator(ctx, listofembed)
                    await paginator.run()
                else : await ctx.send("This Category Maybe is unsuported or underdevelopment")
            if selection.content == "4"and selection.content in sent:
                print("scraping")
                Articlescrape(informantion["link4"])
                if CATEGORIES['category'] == 'character':

                    content = CHARACTERINFO
                    Nama = content["Name"]
                    Img = Scrapeweb.INFO["image4"]
                    tempList = content["General_Info"]
                    separator = "\n"
                    generalinfo= separator.join(tempList)
                    description = content["Description"]
                    ingameDescription = content["Ingame_description"]
                    
                    character1=discord.Embed(title="--------General info--------", description=generalinfo)
                    character1.set_author(name="-----"+Nama+"-----")
                    character1.set_thumbnail(url=Img)
                    character1.add_field(name="Description", value=description, inline=False)
                    character1.add_field(name="Ingame Description", value=ingameDescription, inline=False)
                    
                    character2 = discord.Embed(title="--------------------")
                    character2.set_author(name=".-----Talents-----.")
                    keysTalent = list(CHARACTERINFO["Talents"])
                    for key in keysTalent:
                        talentDesc = [i for i in CHARACTERINFO["Talents"][key]]
                        character2.add_field(name=key, value=separator.join(talentDesc), inline=False)

                    character3 = discord.Embed(title="--------------------")
                    character3.set_author(name=".-----Constelations-----.")
                    keysConst = list(CHARACTERINFO["Constelations"])
                    
                    for key in keysConst:
                        constDesc = [i for i in CHARACTERINFO["Constelations"][key]]
                        character3.add_field(name=key, value=separator.join(constDesc), inline=False)
                    EmbedList = [character1,character2,character3]
                    paginator = BotEmbedPaginator(ctx, EmbedList)
                    await paginator.run()
                if CATEGORIES['category'] == 'weapons':
                    Wname       = WEAPONINFO["Name"]
                    Wimg        = WEAPONINFO["Img"]
                    Winfo       = WEAPONINFO["Info"]
                    Wlore       = WEAPONINFO["Lore"]
                    WabilityT   = WEAPONINFO["Ability"][0]
                    WabilityC   = WEAPONINFO["Ability"][1]
                    Weapon1 = discord.Embed(title="---------------",description=Winfo)
                    Weapon1.set_author(name=Wname)
                    Weapon1.add_field(name=WabilityT, value=WabilityC ,inline=False)
                    Weapon1.set_image(url="https://www.gensh.in"+Wimg)
                    Weapon2 =discord.Embed(title="---------------", description=Wlore)
                    Weapon2.set_author(name="Lore")
                    listofembed = [Weapon1,Weapon2]
                    paginator = BotEmbedPaginator(ctx, listofembed)
                    await paginator.run()
                else : await ctx.send("This Category Maybe is unsuported or underdevelopment")
            # except asyncio.TimeoutError():
            else : print("failed") 
        else: await ctx.send("Sorry, No Result is Found :<")

def setup(client):
    client.add_cog(search(client))