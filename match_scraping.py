import soup_functions

def get_matches(soup):
    matches = soup.find_all('div', class_='ds-mb-2')
    return matches


def get_match_titles(soup, match_index):
    date = get_match_date(soup, match_index)
    team1 = get_team_name_one(soup, match_index)
    # match_title = team1 + " vs " + team2 + " date: " + match_date
    # return match_title

def get_match_date(soup, match_index):
    match_dates = soup.find_all('div', class_= "ds-text-compact-xs ds-font-bold ds-w-24")
    match_date_html = str(match_dates[match_index])
    match_date = match_date_html[53:64]
    return match_date

def get_team_name_one(soup, match_index):
    match = (soup.find_all('div', class_ = "ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1"))[match_index]
    team_html = str(match.find('p', class_ = "ds-text-tight-m ds-font-bold ds-capitalize ds-truncate"))
    team = team_html[66:-4]
    return(team)

def get_team_name_two(soup, match_index):
    match = (soup.find_all('div', class_ = "ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1"))[match_index]
    team_html = str(match.find('p', class_ = "ds-text-tight-m ds-font-bold ds-capitalize ds-truncate"))
    team = team_html[66:-4]
    return(team)

def get_match_url(soup, match_index):
    url = "insertcode"+soup_functions.base_url
    return url