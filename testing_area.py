import scraper

soup = scraper.get_soup()
print(soup[:10])

text = """<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><link rel="preload" href="https://wassets.hscicdn.com/static/fonts/CiIcons/ci-icons"""
