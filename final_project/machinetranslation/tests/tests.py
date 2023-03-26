"""
    tests.py
    Unitary tests for translation.
    :copyright: (c) 2023 Juan Carcedo, All rights reserved
    :licence: MIT.
"""
import unittest
from ..translator import *


class TestTranslationWatsonIBM(unittest.TestCase):

    def test_english_to_french(self):
        watson_api = create_watson_api()
        self.assertEqual(english_to_french(watson_api, "Hello"), "Bonjour")
        self.assertEqual(english_to_french(watson_api), "")

    def test_french_to_english(self):
        watson_api = create_watson_api()
        self.assertEqual(french_to_english(watson_api, "Bonjour"), "Hello")
        self.assertEqual(french_to_english(watson_api), "")


if __name__ == '__main__':
    unittest.main()
