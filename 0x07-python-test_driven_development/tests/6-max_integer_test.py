#!/usr/bin/python3
"""unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''define unittests for max_integer(list=[])'''

    def test_ordered_list(self):
        '''Test an ordered list of integers.'''
        ordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(ordered), 4)

    def test_max_At_Beginning(self):
        '''Test a list with a beginning max value.'''
        max_At_Beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_At_Beginning), 4)

    def test_empty_List(self):
        '''test an empty list.'''
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_Element_List(self):
        '''test a list with asingle element'''
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_Floats(self):
        '''test a list of floats.'''
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        '''test a list of ints and floats'''
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        '''Test a string'''
        string = "bigail"
        self.assertEqual(max_integer(string), 'r')
    
    def test_list_Of_strings(self):
        '''test a list of strings.'''
        strings = ["bigail", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_Empty_String(self):
        '''test an empty string.'''
        self.assertEqual(max_integer(""), None)

  
if __name__ == "__main__":
    unittest.main()
