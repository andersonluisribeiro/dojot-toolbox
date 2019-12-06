import sys
sys.path.append("..")

import unittest
import mock
from lib import Optional

class PersisterTest(unittest.TestCase):

    def test_ask_use_when_answer_is_yes(self):
        with mock.patch('builtins.input', return_value="y"):
            optional = Optional()
            res = optional.ask_use("cron")
            self.assertTrue(optional.ask_use("cron"))

    def test_ask_use_when_answer_is_other(self):
        with mock.patch('builtins.input', return_value="n"):
            optional = Optional()
            res = optional.ask_use("cron")
            self.assertFalse(optional.ask_use("cron"))        

    def test_ask_use_when_answer_is_empty(self):
        with mock.patch('builtins.input', return_value=""):
            optional = Optional()
            res = optional.ask_use("cron")
            self.assertFalse(optional.ask_use("cron"))

if __name__ == '__main__':
    unittest.main()