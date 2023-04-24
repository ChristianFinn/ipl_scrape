import soup_functions
import match_scraping


soup = soup_functions.get_soup()
print(match_scraping.get_match_title(soup))
matches = match_scraping.get_matches(soup)
for match in matches[:1]:
    match_title = match_scraping.get_match_title(match)
    print(match_title)
    