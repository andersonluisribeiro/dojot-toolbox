import sys
sys.path.append("..")

import unittest
from lib import Disk
from unittest.mock import patch

class DiskTest(unittest.TestCase):

    def test_is_free(self):
        with patch('shutil.disk_usage', return_value={'total': 0, 'used': 0, 'free': 10737418240}): #10GB
            disk = Disk()
            self.assertTrue(disk.has_free(5))

    def test_is_available_when_is_not(self):
        with patch('shutil.disk_usage', return_value={'total': 0, 'used': 0, 'free': 10737418240}):  #10GB
            disk = Disk()
            self.assertFalse(disk.has_free(15))    

    def test_is_available_with_value_alocated(self):
        with patch('shutil.disk_usage', return_value={'total': 0, 'used': 0, 'free': 10737418240}):  #10GB
            disk = Disk()
            disk.alocate(8)
            self.assertFalse(disk.has_free(5)) 

    def test_is_available_when_has_less_than_ninety_percent(self):
        with patch('shutil.disk_usage', return_value={'total': 0, 'used': 0, 'free': 10737418240}):  #10GB
            disk = Disk()
            disk.alocate(5)
            self.assertFalse(disk.has_free(4.1))                    


if __name__ == '__main__':
    unittest.main()