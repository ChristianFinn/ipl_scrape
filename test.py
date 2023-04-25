import unittest
import soup_functions
import match_scraping
import data_storing

class Tests(unittest.TestCase):

    def test_get_soup(self):
        soup = str(soup_functions.get_soup())
        soup_sample = (soup[:110])
        soup_expected = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><link as="font" crossorigin="anonymous" href="htt"""
        self.assertEqual(soup_sample, soup_expected)


    def test_get_match_date_one(self):
        date_expected = "Sat, 26 Mar"
        first_date = match_scraping.get_match_date(0)
        self.assertEqual(date_expected, first_date)

    def test_get_match_date_three(self):
        date_expected = "Sun, 27 Mar"
        third_date = match_scraping.get_match_date(2)
        self.assertEqual(date_expected, third_date)

    def test_get_match_date_fifteen(self):
        date_expected = "Thu, 07 Apr"
        fifteenth = match_scraping.get_match_date(14)
        self.assertEqual(date_expected, fifteenth)


    def test_get_team_name_one(self):
        teams_expected = "Chennai Super Kings"
        teams = match_scraping.get_team_name_one(0)
        self.assertEqual(teams_expected, teams)


    def test_get_team_name_one_three(self):
        teams_expected = "Royal Challengers Bangalore"
        teams = match_scraping.get_team_name_one(2)
        self.assertEqual(teams_expected, teams)

    
    def test_get_team_name_one_fifteen(self):
        teams_expected = "Delhi Capitals"
        teams = match_scraping.get_team_name_one(14)
        self.assertEqual(teams_expected, teams)


    def test_get_team_name_two(self):
        teams_expected = "Kolkata Knight Riders"
        teams = match_scraping.get_team_name_two(0)
        self.assertEqual(teams_expected, teams)


    def test_get_team_name_two_three(self):
        teams_expected = "Punjab Kings"
        teams = match_scraping.get_team_name_two(2)
        self.assertEqual(teams_expected, teams)

    
    def test_get_team_name_two_fifteen(self):
        teams_expected = "Lucknow Super Giants"
        teams = match_scraping.get_team_name_two(14)
        self.assertEqual(teams_expected, teams)

    
    def test_abbreviations_dict(self):
        team_abrv_expected = "CSK"
        team = match_scraping.get_team_name_one(0)
        team_abrv = match_scraping.team_name_abbreviations_dict[team]
        self.assertEqual(team_abrv_expected, team_abrv)


    def test_get_teams(self):
        teams_expected = ["CSK", "KKR"]
        teams = match_scraping.get_team_names(0)
        self.assertEqual(teams_expected, teams)


    def test_get_matches(self):
        first_match_title_expected = "CSK vs KKR date: Sat, 26 Mar"
        first_match_title = match_scraping.get_match_titles(0)
        self.assertEqual(first_match_title, first_match_title_expected)


    def test_get_match_url(self):
        url_expected = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/chennai-super-kings-vs-kolkata-knight-riders-1st-match-1304047/full-scorecard"
        url = match_scraping.get_match_url(0)
        self.assertEqual(url, url_expected)


    def test_get_match_url_three(self):
        url_expected = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/punjab-kings-vs-royal-challengers-bangalore-3rd-match-1304049/full-scorecard"
        url = match_scraping.get_match_url(2)
        self.assertEqual(url, url_expected)

    
    def test_get_match_url_fifteen(self):
        url_expected = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/lucknow-super-giants-vs-delhi-capitals-15th-match-1304061/full-scorecard"
        url = match_scraping.get_match_url(14)
        self.assertEqual(url, url_expected)

    
    def test_create_matches_dict(self):
        first_entry_expected = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/chennai-super-kings-vs-kolkata-knight-riders-1st-match-1304047/full-scorecard"
        dict = data_storing.create_matches_url_dict()
        first_entry = dict["CSK vs KKR date: Sat, 26 Mar"]
        self.assertEqual(first_entry_expected, first_entry)

if __name__ == '__main__':
    unittest.main()