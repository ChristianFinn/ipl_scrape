import scraper
import match_scraping


soup = scraper.get_soup()
matches = match_scraping.get_matches(soup)
for match in matches[:1]:
    match_title = match_scraping.get_match_title(match)
    print(match_title)
    