import sys
sys.path.append("..")

import unittest
import mock
from lib import Kafka

class KafkaTest(unittest.TestCase):

    def test_ask_persistence_time_for_user(self):
        with mock.patch('builtins.input', return_value="222"):
            kafka = Kafka().ask_persistence_time()
            self.assertEqual(kafka.persistence_time, 222)

    def test_ask_persistence_time_for_user_default_value(self):
        with mock.patch('builtins.input', return_value=""):
            kafka = Kafka().ask_persistence_time()
            self.assertEqual(kafka.persistence_time, 168) 
            
    def test_ask_persistence_time_for_user_with_no_int_value(self):
        with mock.patch('builtins.input', return_value="xxx"):
            kafka = Kafka().ask_persistence_time()
            self.assertEqual(kafka.persistence_time, 168)                             


if __name__ == '__main__':
    unittest.main()