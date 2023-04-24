import soup_functions

team_name_abbreviations_dict = {"Chennai Super Kings": "CSK", "Delhi Capitals": "DC", "Gujarat Titans": "GT", "Kolkata Knight Riders": "KKR", "Lucknow Super Giants": "LSG", "Mumbai Indians": "MI", "Punjab Kings": "PBKS", "Rajasthan Royals": "RR", "Royal Challengers Bangalore": "RCB", "Sunrisers Hyderabad": "SRH"}

def get_match_titles(soup, match_index):
    date = get_match_date(soup, match_index)
    team1 = get_team_name_one(soup, match_index)
    team2 = get_team_name_two(soup, match_index)
    match_title = team_name_abbreviations_dict[team1] + " vs " + team_name_abbreviations_dict[team2] + " date: " + date
    return match_title

def get_match_date(soup, match_index):
    match_dates = soup.find_all('div', class_= "ds-text-compact-xs ds-font-bold ds-w-24")
    match_date_html = str(match_dates[match_index])
    match_date = match_date_html[53:64]
    i = 1
    while match_date == "</div>":
        match_date_html = str(match_dates[match_index - i])
        match_date = match_date_html[53:64]
        i += 1
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

def get_team_names(soup, match_index):
    teams = []
    team1 = get_team_name_one(soup, match_index)
    teams.append(team_name_abbreviations_dict[team1])
    team2 = get_team_name_two(soup, match_index)
    teams.append(team_name_abbreviations_dict[team2])
    return teams

def get_match_url(soup, match_index):
    match = (soup.find_all('div', class_ = "ds-grow ds-px-4 ds-border-r ds-border-line-default-translucent"))[match_index]
    match_html = (match.find('a', class_ = "ds-no-tap-higlight"))
    pretty_match = match_html.prettify()
    pretty_match_front = pretty_match[36:]
    url_add_on = pretty_match_front.split('"')[0]
    url = soup_functions.base_url + url_add_on
    return url