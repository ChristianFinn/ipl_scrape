import soup_functions
import data_storing

matches_url_dict = data_storing.create_matches_url_dict()

def get_team_batsmen_names(soup, team_no):
    all_batsmen = (soup.find_all('div', class_ = "ds-p-0"))[team_no]
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
    for match in matches_url_dict:
        url = matches_url_dict[match]
        soup = soup_functions.get_soup(url)
        team_1_batsmen = get_team_batsmen_names(soup, 1)
        team_2_batsmen = get_team_batsmen_names(soup, 2)
        print(f"team1: {team_1_batsmen}")
        print(f"team2: {team_2_batsmen}")


get_all_batsmen_detes(matches_url_dict)


