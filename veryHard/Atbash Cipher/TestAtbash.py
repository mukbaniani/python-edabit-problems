import unittest
from atbash import atbash


class TestAtbash(unittest.TestCase):
    def test_atbash(self):
        self.assertEqual(atbash("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")
        self.assertEqual(atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")
        self.assertEqual(atbash("The word 'atbash' derives from the the first and last 2 letters of the Hebrew alphabet."), "Gsv dliw 'zgyzhs' wvirevh uiln gsv gsv urihg zmw ozhg 2 ovggvih lu gsv Svyivd zokszyvg.")
        self.assertEqual(atbash("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi."),"Encryption and decryption are identical for the Atbash cipher.")


if __name__ == '__main__':
    unittest.main()