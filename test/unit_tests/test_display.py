# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""

"""

___authore___ = "Kanisorn Kaewsrithong"


# standard libraries
from datetime import datetime
import os
import sys
import unittest

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import display


class TestDisplay(unittest.TestCase):
    def test_update_line(self):
        """ Test that calling the update_line method
        in display.Display works correctly """
        _display = display.Display(None)
        time = [datetime(2023, 1, 24, 10, 50, 12)]
        temps = [5]
        _display.update_line(time, temps)

        print("getting x y data")
        print(_display.lines[0].get_xydata())

        self.assertEqual(time, _display.lines[0].get_xdata()) # check update_line -> [time] = x_data
        self.assertEqual(temps, _display.lines[0].get_ydata()) # check update_line -> [temp] = y_data



if __name__ == '__main__':
    unittest.main()