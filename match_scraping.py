def get_matches(soup):
    matches = soup.find_all('div', class_='ds-mb-2')
    return matches


def get_match_title(match_soup):

    # team1 = match_soup.ge
    match_date_html = match_soup.find('div', class_= "ds-text-compact-xs ds-font-bold ds-w-24")
    return match_date_html
    #  match_date = match_date_html.text.strip()
    # match_title = team1 + " vs " + team2 + " date: " + match_date
    # print(match_date)
    # return match_title

