import scraper

print("test starting")

soup = scraper.get_soup()
pretty_soup = soup.prettify()
length = len(pretty_soup)
for i in range(length):
    if pretty_soup[i:(i+11)] == "Sat, 26 Mar":
        print("found!!!")
        print(pretty_soup[i-100:i+100])