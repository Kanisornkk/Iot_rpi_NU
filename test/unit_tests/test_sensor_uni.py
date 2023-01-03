# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
"""
___authore___ = "Kanisorn Kaewsrithong"

#standard libraries
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.join("..","..","src","app"))
#local files
from src.app import main_gui
class TestSensorUI(unittest.TestCase):
    def test_button_click_unit(self):
        gui = main_gui.SensorUI()
        print(gui.running)
        self.assertFalse(gui.running)
        gui.button_click()
        print(gui.running)
        self.assertTrue(gui.running)

    def test_button_click_call_status(self):
        with mock.patch("main_gui.comm.MQTTConn") as mocked_comm:
            gui = main_gui.SensorUI()
            gui.button_click()
            gui.comm.publish.assert_called()
            gui.comm.publish: mock.Magicmock
            gui.comm.publish.assert_called_with('On')



if __name__ == '__main__':
    unittest.main()
