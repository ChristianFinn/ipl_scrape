# ipl_scrape
Scrape IPL Match Data

soup_functions.py will retrieve the html for each page.

match_scraping.py creates the title of each match out of the teams playing and the date of the match. It will aslo find the url's for each match.

data_storing.py creates a dictionary with each match title as a key and the url as the value.

match_details_scraping.py performs most of the scraping functions. it loops through the dictionary created in data_storing.py and gets the name, runs, balls faced, 4's, 6's and wether they are out, for each batsmen. These details are looped through in order to create a final dictionary with all details.

dataframe.py takes the final dictionary and turns it into a pandas data frame.