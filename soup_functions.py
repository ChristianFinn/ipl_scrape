import urllib
from urllib import request
from bs4 import BeautifulSoup

base_url = "https://www.espncricinfo.com"
all_matches_url = base_url+"/series/indian-premier-league-2022-1298423/match-results"


def get_soup(url = all_matches_url):
    print(url)
    print("\n")
    url = urllib.request.urlopen(url)
    b = url.read()
    s = b.decode("utf-8")
    soup = BeautifulSoup(s, features="html.parser")
    return soup