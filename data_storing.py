import soup_functions
import match_scraping

matches = {}

soup = soup_functions.get_soup()
matches = soup.find_all('div', class_ = "ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1")

for match in range(len(matches)):
    match_title = match_scraping.get_match_titles(soup, match)
    print(match_title)
    # matches.append()