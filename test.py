import unittest
import scraper

class Tests(unittest.TestCase):

    def test_get_soup(self):
        soup = str(scraper.get_soup())
        soup_sample = (soup[:110])
        soup_expected = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><link as="font" crossorigin="anonymous" href="htt"""
        self.assertEqual(soup_sample, soup_expected)


    def test_get_matches(self):
        soup = str(scraper.get_matches(scraper.get_soup()))
        first_match_ = "#main-container > div.ds-relative > div.lg\:ds-container.lg\:ds-mx-auto.lg\:ds-px-5 > div.ds-flex.ds-space-x-5 > div.ds-grow.ds-px-0 > div.ds-mb-4 > div > div > div > div.ds-p-4.hover\:ds-bg-ui-fill-translucent.ds-border-none.ds-border-t.ds-border-line"
        soup_expected = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><link as="font" crossorigin="anonymous" href="htt"""
        self.assertEqual(soup_sample, soup_expected)

if __name__ == '__main__':
    unittest.main()