# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Test that when data input to the sensor_data.Sensor
it is passed and handled correctly by display.Display
"""

___authore___ = "Kanisorn Kaewsrithong"

# standard libraries
import unittest
import os
import sys
import unittest
from datetime import datetime

sys.path.append(os.path.join("..","..","src","app"))

#local files
from src.app import display
from src.app import sensor_data


class TestDataToDisplay(unittest.TestCase):
    def test_data_to_display(self):
        """
        Test that adding data to the data class makes the
        pyplot graph have the correct xy data
        """
        sensor_class = sensor_data.SensorData(None)
        print(sensor_class)
        # add 1 data point and check it is added correctly
        now = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data(now, 5)
        xy_data = sensor_class.display.lines[0].get_xydata().tolist()
        # TODO: calculate how date time is converted to a float
        self.assertListEqual([[19381.45152777778, 5]], xy_data)



if __name__ == "__main__":
    unittest.main()