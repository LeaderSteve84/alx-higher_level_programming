#!/usr/bin/python3
# 6-max_integer_test.py
'''unittests for max_integer(list=[]).'''

import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_MaxInteger(unittest.TestCase):
    '''define unittests for max_integer(list=[])'''

    def test_ordered_list(self):
        '''Test an ordered list of integers.'''
        ordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(ordered), 4)

    def test_maxAtBeginning(self):
        '''Test a list with a beginning max value.'''
        maxAtBeginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(maxAtBeginning), 4)

    def test_emptyList(self):
        '''test an empty list.'''
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_oneElementList(self):
        '''test a list with asingle element'''
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def testFloats(self):
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
    
    def test_listOf_strings(self):
        '''test a list of strings.'''
        strings = ["bigail", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def testEmptyString(self):
        '''test an empty string.'''
        self.assertEqual(max_integer(""), None)

  
  if __name__ == "__main__":
      unittest.main()

