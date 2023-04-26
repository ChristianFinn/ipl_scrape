import soup_functions
import data_storing

matches_url_dict = data_storing.create_matches_url_dict()

def get_batsmen_names(soup, team_no):
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


def get_runs(soup, team_no, param, player_id = 0):
    if param == "runs":
        html_before = "<strong>"
        start_id = 11
        end_id = 2
        loop_again = False
    elif param == "balls":
        html_before = '-right">'
        start_id = 10
        end_id = 1
        loop_again = True


    value_store = []
    items_to_remove = ['', '\n', '>\n', '>']
    all_batsmen = (soup.find_all('div', class_ = "ds-p-0"))[team_no]
    batsmen = (all_batsmen.find_all('td', class_ = "ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-text-right"))
    for man in batsmen:
        man = man.prettify()
        string_start = False
        for i in range(len(man)):
            if man[i:i+8] == html_before:
                start_i = i + start_id
                string_start = True
            elif string_start and man[i] == "<":
                end_i = i - end_id
                break
        run_num = man[start_i:end_i]
        try:
            value_store.append(int(run_num))
        except:
            items_to_remove.append(run_num)

    if loop_again:
        out = (value_store[(player_id * 4):(player_id * 4) + 4])
    else:
        out = value_store
    return out


def get_all_batsmen_detes(matches_url_dict):
    for match in matches_url_dict:
        url = matches_url_dict[match]
        soup = soup_functions.get_soup(url)
        team_1_batsmen = get_batsmen_names(soup, 1)
        team_2_batsmen = get_batsmen_names(soup, 2)
        team_1_runs = get_runs(soup, 1, "runs")
        team_2_runs = get_runs(soup, 2, "runs")
        team_1_balls = get_runs(soup, 1, "balls")
        team_2_balls = get_runs(soup, 1, "balls")
        print(team_1_balls)


get_all_batsmen_detes(matches_url_dict)