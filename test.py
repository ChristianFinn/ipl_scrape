import unittest
import soup_functions
import match_scraping

class Tests(unittest.TestCase):

    def test_get_soup(self):
        soup = str(soup_functions.get_soup())
        soup_sample = (soup[:110])
        soup_expected = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><link as="font" crossorigin="anonymous" href="htt"""
        self.assertEqual(soup_sample, soup_expected)


    def test_get_match_date_one(self):
        soup = soup_functions.get_soup()
        date_expected = "Sat, 26 Mar"
        first_date = match_scraping.get_match_date(soup, 0)
        self.assertEqual(date_expected, first_date)

    def test_get_match_date_two(self):
        soup = soup_functions.get_soup()
        date_expected = "Sun, 27 Mar"
        first_date = match_scraping.get_match_date(soup, 1)
        self.assertEqual(date_expected, first_date)

    def test_get_match_date_fifteen(self):
        soup = soup_functions.get_soup()
        date_expected = "Thu, 07 Apr"
        first_date = match_scraping.get_match_date(soup, 14)
        self.assertEqual(date_expected, first_date)


    def test_get_team_name_one(self):
        soup = soup_functions.get_soup()
        teams_expected = "Chennai Super Kings"
        teams = match_scraping.get_team_name_one(soup, 0)
        self.assertEqual(teams_expected, teams)


    def test_get_team_name_one_two(self):
        soup = soup_functions.get_soup()
        teams_expected = "Mumbai Indians"
        teams = match_scraping.get_team_name_one(soup, 1)
        self.assertEqual(teams_expected, teams)

    
    def test_get_team_name_one_fifteen(self):
        soup = soup_functions.get_soup()
        teams_expected = "Delhi Capitals"
        teams = match_scraping.get_team_name_one(soup, 14)
        self.assertEqual(teams_expected, teams)


    def test_get_team_name_two(self):
        soup = soup_functions.get_soup()
        teams_expected = "Kolkata Knight Riders"
        teams = match_scraping.get_team_name_two(soup, 0)
        self.assertEqual(teams_expected, teams)


    def test_get_team_name_two_two(self):
        soup = soup_functions.get_soup()
        teams_expected = "Delhi Capitals"
        teams = match_scraping.get_team_name_two(soup, 1)
        self.assertEqual(teams_expected, teams)

    
    def test_get_team_name_two_fifteen(self):
        soup = soup_functions.get_soup()
        teams_expected = "Lucknow Super Giants"
        teams = match_scraping.get_team_name_two(soup, 14)
        self.assertEqual(teams_expected, teams)

    
    def test_abbreviations_dict(self):
        soup = soup_functions.get_soup()
        team_abrv_expected = "CSK"
        team = match_scraping.get_team_name_one(soup, 0)
        team_abrv = match_scraping.team_name_abbreviations_dict[team]
        self.assertEqual(team_abrv_expected, team_abrv)


    def test_get_teams(self):
        soup = soup_functions.get_soup()
        teams_expected = ["CSK", "KKR"]
        teams = match_scraping.get_team_names(soup, 0)
        self.assertEqual(teams_expected, teams)


    def test_get_matches(self):
        soup = soup_functions.get_soup()
        first_match_title_expected = "CSK vs KKR date: Sat, 26 Mar"
        first_match_title = match_scraping.get_match_titles(soup, 0)
        self.assertEqual(first_match_title, first_match_title_expected)


    def test_get_match_url(self):
        soup = soup_functions.get_soup()
        url_expected = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/chennai-super-kings-vs-kolkata-knight-riders-1st-match-1304047/full-scorecard"
        url = match_scraping.get_match_url(soup, 0)
        self.assertEqual(url, url_expected)


    def test_get_match_url_two(self):
        soup = soup_functions.get_soup()
        url_expected = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/delhi-capitals-vs-mumbai-indians-2nd-match-1304048/full-scorecard"
        url = match_scraping.get_match_url(soup, 1)
        self.assertEqual(url, url_expected)

    
    def test_get_match_url_fifteen(self):
        soup = soup_functions.get_soup()
        url_expected = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/lucknow-super-giants-vs-delhi-capitals-15th-match-1304061/full-scorecard"
        url = match_scraping.get_match_url(soup, 14)
        self.assertEqual(url, url_expected)

if __name__ == '__main__':
    unittest.main()