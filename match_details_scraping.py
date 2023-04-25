import soup_functions
import data_storing

matches_url_dict = data_storing.create_matches_url_dict()
# Just doing first match so it doesn't take too long

def get_team_1_batsmen_names(soup):
    all_batsmen = (soup.find_all('div', class_ = "ds-p-0"))[1]
    batsmen = (all_batsmen.find_all('a', class_ = "ds-inline-flex ds-items-start ds-leading-none"))
    names = []
    last_name = False
    for man in batsmen:
        man = man.prettify()
        start_man = False
        for i in range(len(man)):
            if man[i:i+5] == "title":
                starting_i = i+7
                start_man = True
            elif man[i] == ">" and start_man:
                end_i = i-1
                name = man[starting_i:end_i]
                if name in names or name[:9] == "View full":
                    last_name = True
                else: 
                    names.append(name)
                break
        if last_name:
            break
            
    return names


def get_all_batsmen_detes(matches_url_dict):
    i = 0
    batsmen = {}
    for match in matches_url_dict:
        batsmen_data = {}
        url = matches_url_dict[match]
        soup = soup_functions.get_soup(url)
        team_1_batsmen = get_team_1_batsmen_names(soup)


get_all_batsmen_detes(matches_url_dict)

