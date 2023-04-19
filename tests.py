import unittest
import scraper

class Tests(unittest.TestCase):

    def test_get_soup(self):
        soup = scraper.get_soup()
        soup_expected = """<!DOCTYPE html><html lang="en"><head><meta charSet="utf-8"/><link rel="preload" href="https://wassets.hscicdn.com/static/fonts/CiIcons/ci-icons"""
        self.assertEqual(soup_expected, soup[:142])

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()