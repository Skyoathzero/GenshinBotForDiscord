import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

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
    INFO["card_info1"] = newcards[0]
    INFO["card_info2"] = newcards[1]
    INFO["card_info3"] = newcards[2]
    INFO["card_info4"] = newcards[3]
def addtodictIMG(img):
    INFO['image1'] = linktodatabase + img[0]
    INFO['image2'] = linktodatabase + img[1]
    INFO['image3'] = linktodatabase + img[2]
    INFO['image4'] = linktodatabase + img[3]
def addtodictLINKS(links):
    INFO['link1'] = linktodatabase + links[0]
    INFO['link2'] = linktodatabase + links[1]
    INFO['link3'] = linktodatabase + links[2]
    INFO['link4'] = linktodatabase + links[3]
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
    NO_OF_RESULT = noOfRessult[0].get_text()
    print(NO_OF_RESULT)
    addtodictLINKS(refinedlinks)
    addtodictINFO(cards)
    addtodictIMG(refinedimages)



Scrape("pyro")
# print("")
# print(INFO["card_info1"])
# print(INFO["card_info2"])
print(INFO["image1"])
print(INFO["link1"])

