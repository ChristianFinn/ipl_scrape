import soup_functions
import match_scraping



print("test starting")

# team_dict = match_scraping.team_name_abbreviations_dict
# print(team_dict["Chennai Super Kings"])

# soup = soup_functions.get_soup()


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