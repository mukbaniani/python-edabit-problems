import unittest
from security import security


class TestSecurity(unittest.TestCase):
    def test_security(self):
        self.assertEqual(security("xxTxxx$xxxTxxxGxxT"), "ALARM!")
        self.assertEqual(security("xGxx$xxGxxxTTT"), "Safe")
        self.assertEqual(security("TxGxx$xxx$xxxGxxT"), "Safe")
        self.assertEqual(security("GxxxTxxGxxTxx$xx$xxTxxG"), "ALARM!")
        self.assertEqual(security("xxGTxx$xx$xxxxxxG"), "ALARM!")
        self.assertEqual(security("xxTxxxxxxxx$xGxxxxxxT"), "ALARM!")
        self.assertEqual(security("xx$xxGxxxx$xxxxxxxxxxT"), "ALARM!")
        self.assertEqual(security("xxxTxxxxT"), "Safe")
        self.assertEqual(security("xxGxxxGGG"), "Safe")
    