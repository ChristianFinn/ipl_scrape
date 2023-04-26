import pandas as pd
import soup_functions
import match_scraping

def create_matches_url_dict():
    soup = soup_functions.get_soup()
    matches_dict = {}
    matches = soup.find_all('div', class_ = "ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1")
    for match in range(1):
        match_title = match_scraping.get_match_titles(match)
        match_url = match_scraping.get_match_url(match)
        matches_dict[match_title] = match_url

    return matches_dict


def create_player_dict():
    print("code to write here to use match_details_scraping.get_all_batsmen_detes")
    


# df = pd.DataFrame.from_dict(matches_dict, orient='index')
# print(df.head())
