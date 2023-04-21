import urllib
from urllib import request
from bs4 import BeautifulSoup

ipl_2022_url = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-results"


def extract_data():
    soup = get_soup()

    data = []
    matches = get_matches(soup)

    for match in matches:
        match_data = {}
        match_data['batsmen'] = []
        for row in match.find_all('tr', class_='tablebatsmen')[1:]:
            cols = row.find_all('td')
            batsman = {}
            batsman['name'] = cols[0].text
            batsman['runs'] = cols[1].text
            batsman['balls_faced'] = cols[2].text
            batsman['fours'] = cols[3].text
            batsman['sixes'] = cols[4].text
            batsman['is_out'] = cols[5].text
            match_data['batsmen'].append(batsman)
        data.append(match_data)

    return data

def get_soup():
    url = urllib.request.urlopen(ipl_2022_url)
    b = url.read()
    s = b.decode("utf-8")
    soup = BeautifulSoup(s, features="html.parser")
    return soup