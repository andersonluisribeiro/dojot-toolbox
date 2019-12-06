import sys
sys.path.append("..")

import unittest
import mock
from lib import Persistent

class PersistentTest(unittest.TestCase):

    def test_ask_persistence_when_answer_is_yes(self):
        with mock.patch('builtins.input', return_value="y"):
            persistent = Persistent()
            self.assertTrue(persistent.ask_persistence_volume("cron"))

    def test_ask_persistence_when_answer_is_other(self):
        with mock.patch('builtins.input', return_value="n"):
            persistent = Persistent()
            self.assertFalse(persistent.ask_persistence_volume("cron"))        

    def test_ask_persistence_when_answer_is_empty(self):
        with mock.patch('builtins.input', return_value=""):
            persistent = Persistent()
            self.assertFalse(persistent.ask_persistence_volume("cron"))

    def test_ask_volume_size(self):
        with mock.patch('builtins.input', return_value="222"):
            persistent = Persistent()
            res = persistent.ask_volume_size()
            self.assertEqual(res, 222)          


if __name__ == '__main__':
    unittest.main()