#-*- coding: utf-8 -*-
import unittest
from transliterator import get_transliteration_as_pattern as gtap
from re import match

class TestStringMethods(unittest.TestCase):

    def test_arabic_to_english(self):
        arabic = u"\u0645\u0631\u062d\u0628\u0627"
        english = "marhaban"
        pattern = gtap(arabic, from_="arabic", to_="english")
        self.assertTrue(match(pattern, english))

    def test_english_to_arabic(self):
        arabic = u"\u0645\u0631\u062d\u0628\u0627"
        english = "marhaban"
        pattern = gtap(english, from_="english", to_="arabic")
        self.assertTrue(match(pattern, arabic))


if __name__ == '__main__':
    unittest.main()
