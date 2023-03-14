# copyright (c) 2022 Kanisorn Kaewsrithong <kanisornka65@nu.ac.th>

"""
Unit test the comm file
"""

___authore___ = "Kanisorn Kaewsrithong"

import unittest

class Receive:
    def __init__(self):
        self.data = Data()

    def get_data(self, _data):
        print("get data")
        self.data.add_data(_data)
        return 0


class Data:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        print('add data')
        self.data.append(data)
        return 0


class TestReceive(unittest.TestCase):
    def test_receive_get_data(self):
        """ Unit Test that the get_data method in the class Receive
            will properly call """
        print('\n--------------------------- test_receive_get_data ------------------------------------')
        receive = Receive()
        test_data = 1222
        receive.get_data(test_data)
        print(receive.data.data)
        self.assertListEqual(receive.data.data, [test_data])







class TestData(unittest.TestCase):
    def test_data(self):
        """ Unit Test that the add_data method appends the
            data to the .data attribute """
        print('\n--------------------------- test_rx_to_data ------------------------------------')
        data = Data()
        data_testing_add = 'test data'
        data.add_data(data_testing_add)
        print(data.data)
        self.assertListEqual(data.data, [data_testing_add])


class TestReceiveToData(unittest.TestCase):
    def test_rx_to_data(self):
        """ Integration test that sending data using the
            get_data method in the Receive class will
            correctly append it to the data attribute of
            the Data class """
        print('\n--------------------------- test_rx_to_data ------------------------------------')
        receive = Receive()
        data = Data()
        data_testing = 'test 333'

        print()
