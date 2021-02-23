import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
def toText(isi):
    return isi.get_text()
fakeheader ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
Searchbar1 = "https://www.gensh.in/database?tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40extension%5D=AwsmDatabase&tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40vendor%5D=AWSM&tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40controller%5D=Search&tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40action%5D=quicksearch&tx_awsm_database_gidbsearch%5B__referrer%5D%5Barguments%5D=YTowOnt9ab12f14b058d7f0afc3ee521eecd856b82073eec&tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40request%5D=a%3A4%3A%7Bs%3A10%3A%22%40extension%22%3Bs%3A12%3A%22AwsmDatabase%22%3Bs%3A11%3A%22%40controller%22%3Bs%3A6%3A%22Search%22%3Bs%3A7%3A%22%40action%22%3Bs%3A11%3A%22quicksearch%22%3Bs%3A7%3A%22%40vendor%22%3Bs%3A4%3A%22AWSM%22%3B%7D0a680789a8fd4255931546477c50d2e2f3c4f6ae&tx_awsm_database_gidbsearch%5B__trustedProperties%5D=a%3A2%3A%7Bs%3A10%3A%22searchterm%22%3Bi%3A1%3Bs%3A6%3A%22filter%22%3Ba%3A1%3A%7Bs%3A11%3A%22quicksearch%22%3Bi%3A1%3B%7D%7D01a0a65640549685085443cca595904d6416f72e&tx_awsm_database_gidbsearch%5Bsearchterm%5D="
Searchbar2 = "&tx_awsm_database_gidbsearch%5Bfilter%5D%5Bquicksearch%5D=true"
NO_OF_RESULT = 0
INFO = {"card_info1":"","image1":"","link1":"",
        "card_info2":"","image2":"","link2":"",
        "card_info3":"","image3":"","link3":"",
        "card_info4":"","image4":"","link4":""}
linktodatabase = 'https://www.gensh.in'
def addtodictINFO(cards):
    newcards = [card.get_text() for card in cards]
    try:
        INFO["card_info1"] = newcards[0]
    except : INFO["card_info1"] = ""
    try:
        INFO["card_info2"] = newcards[1]
    except : INFO["card_info2"] = ""
    try:
        INFO["card_info3"] = newcards[2]
    except : INFO["card_info3"] = ""
    try:
        INFO["card_info4"] = newcards[3]
    except : INFO["card_info4"] = ""
def addtodictIMG(img):
    try:
        INFO['image1'] = linktodatabase + img[0]
    except : INFO['image1'] = ""
    try:
        INFO['image2'] = linktodatabase + img[1]
    except : INFO['image2'] = ""
    try:
        INFO['image3'] = linktodatabase + img[2]
    except : INFO['image3'] = ""
    try:
        INFO['image4'] = linktodatabase + img[3]
    except : INFO['image4'] = ""
def addtodictLINKS(links):
    try:
        INFO['link1'] = linktodatabase + links[0]
    except : INFO['link1'] = ""
    try:
        INFO['link2'] = linktodatabase + links[1]
    except : INFO['link2'] = ""
    try:
        INFO['link3'] = linktodatabase + links[2]
    except : INFO['link3'] = ""
    try:
        INFO['link4'] = linktodatabase + links[3]
    except : INFO['link4'] = ""
    
def Scrape(query):
    search = requests.get(Searchbar1 + query + Searchbar2,headers=fakeheader).text
    soup = BeautifulSoup(search,'html.parser')
    searchresult = soup.find('div',attrs={'class' :'col-12 dbsearch-result'})
    cardcontainer= searchresult.find('div',attrs={'class' : 'row'})
    noOfRessult = searchresult.find_all("p",string=re.compile('Results'))
    
    cards = cardcontainer.find_all('div',attrs={"class":"col-12 m-3"})
    
    images = cardcontainer.find_all("img",attrs={"class":"img-icon"})

    links = cardcontainer.find_all('a')

    refinedlinks = [link["href"]for link in links]
    for i in refinedlinks: print(i)

    refinedimages = [image["src"]for image in images]
    # for i in refinedimages: print(i)
    #print(cardcontainer.prettify())
    #print(searchresult.prettify())

    #print(noOfRessult[0])
    #print(cardcontainer.get_text())
    global NO_OF_RESULT
    NO_OF_RESULT = noOfRessult[0].get_text()
    
    addtodictLINKS(refinedlinks)
    addtodictINFO(cards)
    addtodictIMG(refinedimages)
isian = "https://www.gensh.in/characters/amberr"
datatest = "/"
formatres = ""
CATEGORIES = {"category":""}
CHARACTERINFO = {'Name': '',
                'MainIMG':'',
                'General_Info':'',
                'Description':'',
                'Ingame_description':'',
                'Story':'',
                'Talents':'',
                'Constelations':''}
WEAPONINFO = {"Name":"",
            "Img":"",
            "Info":"",
            "Lore":"",
            "Ability":"",
            }
ITEMINFO = {"Name":"",
            "Img":"",
            "Info":""}
ENEMIESINFO = {"Name": "",
                "Img":"",
                "Drops":"",
                "Info":"",
                "Description":""}   
def Articlescrape(isian):

    search = requests.get(isian).text
    soup = BeautifulSoup(search,'html.parser')
    contentclasifier = isian.split("/")
    db = "database"
    if contentclasifier[3] == db :
        if contentclasifier[4]=="npc":
            pass
        if contentclasifier[4]=="quest":
            pass
        if contentclasifier[4]=="artifact-set":
            pass
        if contentclasifier[4]=="enemies":
            enemiescontainer = soup.find_all("div",attrs={"class":"row mb-4"})
            
            container1 = enemiescontainer[0]
            container2 = enemiescontainer[1]
            Name = container1.find("h2")
            infocontainer = container1.find('ul')
            info = infocontainer.find_all("li")
            info = [i.get_text() for i in info ]
            separator = "\n"
            Info = separator.join(info)
            Imagecontainer = container1.find_all("div",attrs={"class":"card-body"})
            Image = Imagecontainer[1].find("img")
            Image = Image["src"]
            
            dropscontainer = container2.find("div",attrs={"class":"col-sm-12 col-lg-4"})
            drops = dropscontainer.find_all("li")
            drops = [i.get_text() for i in drops]
            Drops = separator.join(drops)
            lorecontainer = container2.find("div",attrs={"class":"col-sm-12 col-lg-8"})
            
            lore = lorecontainer.find("div",attrs={"class":"card-body"})
            Lore = lore.get_text()
            # ENEMIESINFO = {"Name": "",
            #     "Img":"",
            #     "Drops":"",
            #     "Info":"",
            #     "Description":""}   
            ENEMIESINFO["Name"]=Name
            ENEMIESINFO["Img"]=Image
            ENEMIESINFO["Drops"]=Drops
            ENEMIESINFO["Info"]=Info
            ENEMIESINFO["Description"]=Lore 
            CATEGORIES["category"] = "enemies"
            print(ENEMIESINFO)        
        if contentclasifier[4]=="consumable":
            consumablecontainer = soup.find("section")
            infocontainer = consumablecontainer.find("div",attrs={"class":"row mb-4"})
            name = lambda x : x.get_text()
            name = name(infocontainer.find("h2"))
            
            descriptionContainer = infocontainer.find_all('li')
            separator = '\n'
            description = [i.get_text() for i in descriptionContainer] 
            description = separator.join(description)
            
            imgcontainer = infocontainer.find("img")
            img = imgcontainer["src"]
            print(img)
        if contentclasifier[4]=="domain":
            pass
        if contentclasifier[4]=="book":
            pass
        if contentclasifier[4]=="artifact":
            pass
        if contentclasifier[4]=="item":
            itemcontainer = soup.find("div",attrs={"class":"row mb-4"})
            Name = itemcontainer.find("h2")
            infocontainer = itemcontainer.find("ul")
            separator = '\n'
            info = infocontainer.find_all("li")
            info = [i.get_text() for i in info]
            info = separator.join(info)
            Imagecontainer = itemcontainer.find("div",attrs={"class":"col-sm-12 col-md-3 text-center"}) 
            Image = Imagecontainer.find("img")
            Image = Image["src"]
            ITEMINFO["Name"] = Name.get_text()
            ITEMINFO["Img"] = Image 
            ITEMINFO["Info"] = info
            CATEGORIES["category"] = "item"

            print(ITEMINFO)
        if contentclasifier[4]=="weapon":

            WeaponDlCr1 = soup.find_all('div',attrs={'class':'row mb-4'})
            WeaponDlCr2 = soup.find('section',attrs={'class':'content'}) 
            WeaponDetailContainer1 = WeaponDlCr1[0]
            WeaponDetailContainer2 = WeaponDlCr2.select("section > div")[1]
            WeaponDetailContainer3 = WeaponDlCr1[1] 

            Name = WeaponDetailContainer1.find("h2")
            Name = Name.get_text()

            Imagecontainer = WeaponDetailContainer1.find("img")
            Image = Imagecontainer["src"]
            
            infocontainer = WeaponDetailContainer1.find("ul") 
            info = infocontainer.find_all("li")
            newinfo = [i.get_text() for i in info]
            separator = "\n"
            info = separator.join(newinfo)

            lorecontainer = WeaponDetailContainer2.find("div",attrs={"class":"card-body"})
            lore = lorecontainer.find_all("p")
            newlore = [i.get_text() for i in lore]
            newlore = separator.join(newlore)
            

            abilitiescontainer = WeaponDetailContainer2.find("div",attrs={"class":"col-sm-12 col-lg-5 mb-4"})
            abilityname = abilitiescontainer.find("p")
            abilitydescription = abilitiescontainer.find("li")
            abilityname = abilityname.get_text()
            abilitydescription = abilitydescription.get_text()
            
            WEAPONINFO["Name"] = Name
            WEAPONINFO["Img"] = Image
            WEAPONINFO["Info"] = info
            WEAPONINFO["Lore"] = newlore
            WEAPONINFO["Ability"] = list((abilityname,abilitydescription))
            CATEGORIES["category"] = "weapons"
            print(WEAPONINFO)
    if contentclasifier[3] == "characters" :
        characterDetailContainer = soup.find("div",attrs={"class": "character-detail"})
        characterDetails = characterDetailContainer.find_all("div",attrs={"class": "row mb-4"})
        
        name = characterDetails[0].find("h2")
        mainImg = characterDetails[0].find("img",attrs ={"class":"img-fluid"})
        CHARACTERINFO["Name"]= toText(name)
        CHARACTERINFO["MainIMG"] = linktodatabase + mainImg["src"]
        
        generalinfoContainer = characterDetails[1].find_all("li")
        generalInfo = [i.get_text() for i in generalinfoContainer]
        CHARACTERINFO["General_Info"] = generalInfo
        
        descriptionContainer = characterDetails[2].find_all("div",attrs={'class':'card'})
        description = descriptionContainer[0].find('div',attrs={"class":"card-body"}).get_text()
        ingameDescription = descriptionContainer[1].find('div',attrs={"class":"card-body"}).get_text()
        CHARACTERINFO["Description"] = description
        CHARACTERINFO["Ingame_description"] = ingameDescription

        loreContainer = characterDetails[4].find('div',attrs={"id":"characterlore"})
        lore = loreContainer.get_text()
        pattern1 = re.compile("Character Story 1")
        pattern2 = re.compile("Character Story 2")
        pattern3 = re.compile("Character Story 3")
        pattern4 = re.compile("Character Story 4")
        pattern5 = re.compile("Character Story 5")
        splittedLore = ['','','','','']
        patternContainer = [pattern1,pattern2,pattern3,pattern4,pattern5]
        num = 0
        tempLore = lore
        for pattern in patternContainer:
            
            # print(lore[:50])
            temporaryList = re.split(pattern,tempLore)
            
            #details,story
            splittedLore[num] = temporaryList[0]
            # print(temporaryList[0][:50])
            temporaryList.pop(0)
            tempLore = temporaryList[0]
            # print(temporaryList[0][:50])
            temporaryList.clear()
            num += 1
        
        
        if splittedLore[0] != '':
            tempList = lambda string : re.split("s",string,maxsplit=1).pop(1)
            splittedLore[0] = tempList(splittedLore[0])
        CHARACTERINFO["Story"] = splittedLore
        skillandConstContainer = characterDetails[6].find('div',attrs={'class':'tab-content'})
        talentContainer = skillandConstContainer.find('div',attrs={'id':'skills'})
        constelationContainer = skillandConstContainer.find('div',attrs={'id':'constellation'})
        ascensionContainer =  skillandConstContainer.find('div',attrs={'id':'ascension'})
        statsContainer = skillandConstContainer.find('div',attrs={'id':'stats'})
        
        TALENT_DICT = {}
        talents = talentContainer.find_all("div",attrs={'class':'row'})
        for i in talents:
            talent = i.find('div',attrs='col-xs-10 col-sm-10 col-md-10 col-lg-10 col-xl-11 col-xxl-11')
            name = talent.find('h4').get_text()
            description = talent.find_all("p")
            description = [x.get_text() for x in description]
            TALENT_DICT[name] = description
        CHARACTERINFO["Talents"] = TALENT_DICT
        keysTalent = list(CHARACTERINFO["Talents"])
        #IMPORTANT
        CONSTELATION_DICT = {}
        constelations = constelationContainer.find_all("div",attrs={'class':'row'})
        for i in constelations:
            constelation = i.find('div',attrs='col-xs-10 col-sm-10 col-md-10 col-lg-10 col-xl-11 col-xxl-11')
            name = constelation.find('h4').get_text()
            print(name)
            description = constelation.find_all("p")
            print(description)
            description = [x.get_text() for x in description]
            for i in description: print(i)
            CONSTELATION_DICT[name] = description
        CHARACTERINFO["Constelations"] = CONSTELATION_DICT
        keysConst = list(CHARACTERINFO["Constelations"])
        CATEGORIES["category"] = "character"
    if contentclasifier[3] == "mechanics" :
        pass
    
    

# CHARACTERINFO = {'Name': '',
#                 'MainIMG':'',
#                 'General_Info':'',
#                 'Description':'',
#                 'Ingame_description':'',
#                 'Story':'',
#                 'Talents':'',
#                 'Constelations':''}
Articlescrape("https://www.gensh.in/database/consumable/adeptus-temptation")

