# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Run unit tests on this StatusButton class in the main_gui file
"""

___authore___ = "Kanisorn"

#standard libraries
import os
import sys
import unittest

#print(os.getcwd())
#print(os.path.abspath(os.path.join("..","..","src","app")))'

sys.path.append(os.path.join("..","..","src","app"))
print(sys.path)
#local files
from src.app import main_gui

#class TestStatusButton(unittest.TestCase):
 #   def test_toggle_color(self):
  #      pass

class TestStatusButton(unittest.TestCase):
    def test_toggle_color(self):
        status_button = main_gui.StatusButton(None, "Tao")
        print(status_button)
        color = (status_button.canvas.itemcget(status_button.circle,
                                            'fill'))
        self.assertEqual(color, "red",
                         msg="status color not changed collectly")
        self.assertEqual(status_button.color, "red",
                         msg="statusButton color not changed collectly")
        status_button.toggle_color(True)
        color = (status_button.canvas.itemcget(status_button.circle,
                                               'fill'))
        self.assertEqual(status_button.color,"green",
                         msg = "status button color not changed collectly")
        self.assertEqual(color, "green",
                         msg="status button color not changed collectly")

        status_button.toggle_color(False)
        color = (status_button.canvas.itemcget(status_button.circle,
                                               'fill'))
        self.assertEqual(status_button.color, "red",
                         msg="status button color not changed collectly")
        self.assertEqual(color, "red",
                         msg="status button color not changed collectly")


if __name__ == '__main__':
    unittest.main()
