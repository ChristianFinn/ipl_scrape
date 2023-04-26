import soup_functions
import match_scraping
import data_storing
import pickle
import pandas as pd



print("test starting")

with open('ipl_data.pickle', 'rb') as handle:
    b = pickle.load(handle)

print(b)

# dict_ = {'key 1': 'value 1', 'key 2': 'value 2', 'key 3': 'value 3'}
# df = pd.DataFrame([dict_])
# print(df.head())

# data = data_storing.create_matches_url_dict()
# for match in data:
#     print(match)

# def prac_func(a = 5):
#     print(a)

# prac_func(2)

# team_dict = match_scraping.team_name_abbreviations_dict
# print(team_dict["Chennai Super Kings"])

# soup = soup_functions.get_soup()
# match_index = 0



# match_scraping.get_match_url(soup, match_index)

# team_html = str(match.find('p', class_ = "ds-text-tight-m ds-font-bold ds-capitalize ds-truncate"))
# team = team_html[66:-4]



# print(match_scraping.get_team_name_one(soup, 0))

# team = match_scraping.get_team_names(soup, 0)
# print(team)
# pretty_soup = soup.prettify()
# length = len(pretty_soup)
# for i in range(length):
#     if pretty_soup[i:(i+3)] == "CSK":
#         print("found!!!")
#         print(pretty_soup[i-400:i+100])


# def extract_data():
#     soup = get_soup()

#     data = []
#     matches = get_matches(soup)

#     for match in matches:
#         match_data = {}
#         match_data['batsmen'] = []
#         for row in match.find_all('tr', class_='tablebatsmen')[1:]:
#             cols = row.find_all('td')
#             batsman = {}
#             batsman['name'] = cols[0].text
#             batsman['runs'] = cols[1].text
#             batsman['balls_faced'] = cols[2].text
#             batsman['fours'] = cols[3].text
#             batsman['sixes'] = cols[4].text
#             batsman['is_out'] = cols[5].text
#             match_data['batsmen'].append(batsman)
#         data.append(match_data)

#     return data

# pretty_soup = soup.prettify()
# for i in range(len(pretty_soup)):
#     if pretty_soup[i:i+14] == """abbreviation":""":
#         teams.append(pretty_soup[i+15:i+18])