import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

fakeheader ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
Searchbar1 = "https://www.gensh.in/database?tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40extension%5D=AwsmDatabase&tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40vendor%5D=AWSM&tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40controller%5D=Search&tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40action%5D=quicksearch&tx_awsm_database_gidbsearch%5B__referrer%5D%5Barguments%5D=YTowOnt9ab12f14b058d7f0afc3ee521eecd856b82073eec&tx_awsm_database_gidbsearch%5B__referrer%5D%5B%40request%5D=a%3A4%3A%7Bs%3A10%3A%22%40extension%22%3Bs%3A12%3A%22AwsmDatabase%22%3Bs%3A11%3A%22%40controller%22%3Bs%3A6%3A%22Search%22%3Bs%3A7%3A%22%40action%22%3Bs%3A11%3A%22quicksearch%22%3Bs%3A7%3A%22%40vendor%22%3Bs%3A4%3A%22AWSM%22%3B%7D0a680789a8fd4255931546477c50d2e2f3c4f6ae&tx_awsm_database_gidbsearch%5B__trustedProperties%5D=a%3A2%3A%7Bs%3A10%3A%22searchterm%22%3Bi%3A1%3Bs%3A6%3A%22filter%22%3Ba%3A1%3A%7Bs%3A11%3A%22quicksearch%22%3Bi%3A1%3B%7D%7D01a0a65640549685085443cca595904d6416f72e&tx_awsm_database_gidbsearch%5Bsearchterm%5D="
Searchbar2 = "&tx_awsm_database_gidbsearch%5Bfilter%5D%5Bquicksearch%5D=true"

NO_OF_RESULT = 0
INFO_1 = {}
INFO_2 = {}
INFO_3 = {}
INFO_4 = {}

def Scrape(query):
    search = requests.get(Searchbar1 + query + Searchbar2,headers=fakeheader).text
    soup = BeautifulSoup(search,'html.parser')
    searchresult = soup.find('div',attrs={'class' :'col-12 dbsearch-result'})
    cardcontainer= searchresult.find('div',attrs={'class' : 'row'})
    noOfRessult = searchresult.find_all("p",string=re.compile('Results'))
    cards = cardcontainer.find_all('div',attrs={"class":"col-12 m-3"})
    #print(cardcontainer.prettify())
    #print(searchresult.prettify())

    #print(noOfRessult[0])
    #print(cardcontainer.get_text())
    NO_OF_RESULT = noOfRessult
    for card in cards:
        print(card.prettify())
    for card in cards:
        print(card.get_text())


Scrape("hydro")

