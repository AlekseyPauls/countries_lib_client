# -*- coding: utf-8 -*-
import unittest
from country_client import normalize_country_name, match_country_name, del_country_name


class NormalizeCountryNameTestCase(unittest.TestCase):

    def test_simple_name(self):
        self.assertEqual(normalize_country_name(url, 'Russia'), 'Russia')

    def test_punctuation_sensitivity(self):
        self.assertEqual(normalize_country_name(url, 'Russia!!!:)'), 'Russia')

    def test_upper_register(self):
        self.assertEqual(normalize_country_name(url, 'RUSSIA'), 'Russia')

    def test_low_register(self):
        self.assertEqual(normalize_country_name(url, 'russia'), 'Russia')

    def test_missed_letter(self):
        self.assertEqual(normalize_country_name(url, 'Rusia'), 'Russia')

    def test_excess_letter(self):
        self.assertEqual(normalize_country_name(url, 'Russiaa'), 'Russia')

    def test_another_letter(self):
        self.assertEqual(normalize_country_name(url, 'Rassia'), 'Russia')

    def test_simple_two_words_name(self):
        self.assertEqual(normalize_country_name(url, 'Russian Federation'), 'Russia')

    def test_excess_word_name(self):
        self.assertEqual(normalize_country_name(url, 'The Russia'), 'Russia')

    def test_american_paris_like_construction(self):
        self.assertEqual(normalize_country_name(url, 'Paris, USA'), 'United States')

    def test_standard_accuracy_result(self):
        self.assertEqual(normalize_country_name(url, 'azazaza'), 'None')

    def test_correct_accuracy_type(self):
        self.assertEqual(normalize_country_name(url, 'Russia', 0.9), 'Russia')

    def test_incorrect_accuracy_type(self):
        self.assertEqual(normalize_country_name(url, 'Russia', '0.7'), 'Invalid argument type')
        self.assertEqual(normalize_country_name(url, 'Russia', []), 'Invalid argument type')

    def test_incorrect_accuracy_value(self):
        self.assertEqual(normalize_country_name(url, 'Russia', 3.0), 'Invalid argument type')
        self.assertEqual(normalize_country_name(url, 'Russia', -0.5), 'Invalid argument type')


class MatchAndDelCountryNameTestCase(unittest.TestCase):

    def test_non_existing_object_delete(self):
            del_country_name(url, 'SpecialNameForTest')
            self.assertEqual(normalize_country_name(url, 'SpecialNameForTest'), 'None')

    def test_match(self):
            match_country_name(url, 'SpecialNameForTest', 'SpecialNameForTest')
            self.assertEqual(normalize_country_name(url, 'SpecialNameForTest'), 'SpecialNameForTest')

    def test_existing_object_delete(self):
            del_country_name(url, 'SpecialNameForTest')
            self.assertEqual(normalize_country_name(url, 'SpecialNameForTest'), 'None')

    def test_correct_priority_match(self):
            match_country_name(url, 'SpecialNameForTest', 'SpecialNameForTest', 1)
            self.assertEqual(normalize_country_name(url, 'SpecialNameForTest'), 'SpecialNameForTest')
            del_country_name(url, 'SpecialNameForTest')

    def test_incorrect_priority_match(self):
        self.assertEqual(match_country_name(url, 'SpecialNameForTest', 'SpecialNameForTest', 3), 'Invalid argument type')
        self.assertEqual(match_country_name(url, 'SpecialNameForTest', 'SpecialNameForTest', -5), 'Invalid argument type')
        self.assertEqual(match_country_name(url, 'SpecialNameForTest', 'SpecialNameForTest', 1.2), 'Invalid argument type')
        self.assertEqual(match_country_name(url, 'SpecialNameForTest', 'SpecialNameForTest', '1'), 'Invalid argument type')
        self.assertEqual(match_country_name(url, 'SpecialNameForTest', 'SpecialNameForTest', []), 'Invalid argument type')

    def test_incorrect_match(self):
        self.assertEqual(match_country_name(url, 1, 'SpecialNameForTest'), 'Invalid argument type')
        self.assertEqual(match_country_name(url, 'SpecialNameForTest', 1), 'Invalid argument type')
        self.assertEqual(match_country_name(url, [], 'SpecialNameForTest'), 'Invalid argument type')
        self.assertEqual(match_country_name(url, 'SpecialNameForTest', []), 'Invalid argument type')

    def test_incorrect_delete(self):
        self.assertEqual(del_country_name(url, 1), 'Invalid argument type')
        self.assertEqual(del_country_name(url, 1.5), 'Invalid argument type')
        self.assertEqual(del_country_name(url, []), 'Invalid argument type')


if __name__ == '__main__':
    print('Input server URL: ')
    url = input()
    unittest.main()
