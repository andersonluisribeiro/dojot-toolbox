import sys
sys.path.append("..")

import unittest
import mock
from lib import Gui

class GuiTest(unittest.TestCase):

    def test_return_vars(self):
        gui = Gui()
        self.assertEqual(gui.vars['use_gui'], False)
        self.assertEqual(gui.vars['gui_replicas'], 1)              


if __name__ == '__main__':
    unittest.main()