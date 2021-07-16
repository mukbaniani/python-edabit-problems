import unittest
from same_vowel_group import same_vowel_group


class TestSomeVowelGroup(unittest.TestCase):
    def test_same_vowel_group(self):
        self.assertEqual(same_vowel_group(["hoops", "chuff", "bot", "bottom"]), 
        ["hoops", "bot", "bottom"])
        self.assertEqual(same_vowel_group(["crop", "nomnom", "bolo", "yodeller"]), 
        ["crop", "nomnom", "bolo"])
        self.assertEqual(same_vowel_group(["semantic", "aimless", "beautiful", "meatless icecream"]), 
        ["semantic", "aimless", "meatless icecream"])
        self.assertEqual(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]), 
        ["many"])
        self.assertEqual(same_vowel_group(["toe", "ocelot", "maniac"]), ["toe", "ocelot"])
        self.assertEqual(same_vowel_group(["a", "apple", "flat", "map", "shark"]), ["a", "flat", "map", "shark"])
        self.assertEqual(same_vowel_group(["a", "aa", "ab", "abc", "aaac", "abe"]), ["a", "aa", "ab", "abc", "aaac"])


if __name__ == '__main__':
    unittest.main()