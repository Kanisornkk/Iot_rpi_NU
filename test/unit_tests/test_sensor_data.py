# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Test the methods of the sensor_data.SensorData class
"""

___authore___ = "Kanisorn Kaewsrithong"

# standard libraries
from datetime import datetime
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.join("..", "..", "src", "app"))
# local files
from src.app import sensor_data


class TestSensorData(unittest.TestCase):
    def setUp(self) -> None:
        """
        For each test, make the sensor class, initialize the temperature
         and time variables and mock the display and put in self to use
         for tests
          """
        with mock.patch("sensor_data.display.Display") as mock_display:
            self.sensor_class = sensor_data.SensorData(None)
            self.sensor_class.temperature = []
            self.sensor_class.time = []
            self.mock_display = mock_display

    def test_add_data(self):
        sensor_class = self.sensor_class
        print(sensor_class)
        # add 1 data point and check it is added correctly
        now = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data(now, 5)
        self.assertEqual([now], sensor_class.time)
        self.assertEqual([5], sensor_class.temperature)
        # add second data point
        now2 = datetime(2023, 1, 24, 10, 51, 12)
        sensor_class.add_data(now2, 10)
        print(f"time: {sensor_class.time}")
        print(f"temp: {sensor_class.temperature}")
        self.assertEqual([now, now2], sensor_class.time)
        self.assertEqual([5, 10], sensor_class.temperature)

    def test_display_update_line_called(self):
        """ Test that the update_line method is called correctly.
         Use the test_sensor_ui code for an example """
        # mock the display.Display class in the sensor_data module
        sensor_class = self.sensor_class
        # add 1 data point and check it is added correctly
        now = datetime(2023, 1, 24, 10, 50, 12)
        sensor_class.add_data(now, 5)

        # check that the self.display.update_line is called with the correct arguments
        sensor_class.display.update_line.assert_called_with([now], [5])


if __name__ == '__main__':
    unittest.main()