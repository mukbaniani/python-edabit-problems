import unittest
from find_pattern import find_pattern


class TestFindPattern(unittest.TestCase):
    def test_find_pattern(self):
        self.assertEqual(find_pattern({
        "Phrase1": 'Made in China',
        "Phrase2": 'Made in Brazil',
        "Phrase3": 'Made in America',
        "Phrase4": 'Made in Colombia',
        }, 'Jhonson'), ['Phrase1 = None', 'Phrase2 = None', 'Phrase3 = None', 'Phrase4 = None'])
	
        self.assertEqual(find_pattern({
                "Phrase1": 'Edabit is great',
                "Phrase2": 'Edabit is very great',
                "Phrase3": 'Edabit is really great',
            }, 'really'), ['Phrase1 = None', 'Phrase2 = None', 'Phrase3 = really'])
            
        self.assertEqual(find_pattern({
                "Phrase1": 'COVID-19 is no good',
                "Phrase2": 'COVID-18 is no good',
                "Phrase3": 'COVID-17 is no good',
            }, 'COVID-19'), ['Phrase1 = COVID-19', 'Phrase2 = None', 'Phrase3 = None'])

        self.assertEqual(find_pattern({
                "Phrase1": 'Made12 in China',
                "Phrase2": 'Made in Brazil',
                "Phrase3": '32Made in America',
                "Phrase4": 'Made in Colombia',

            }, 'Made'), ['Phrase1 = Made', 'Phrase2 = Made', 'Phrase3 = Made', 'Phrase4 = Made'])

if __name__ == '__main__':
    unittest.main()
