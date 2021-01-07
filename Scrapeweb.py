import requests
from bs4 import BeautifulSoup

Searchbar = "https://genshin-impact.fandom.com/wiki/Special:Search?query="
def Scrape(query):
    search = requests.get(Searchbar + query).text
    soup = BeautifulSoup(search,'lxml')
    print(soup.prettify())

Scrape("hydro")