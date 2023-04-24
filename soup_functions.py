import urllib
from urllib import request
from bs4 import BeautifulSoup

ipl_2022_url = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-results"


def get_soup():
    url = urllib.request.urlopen(ipl_2022_url)
    b = url.read()
    s = b.decode("utf-8")
    soup = BeautifulSoup(s, features="html.parser")
    return soup