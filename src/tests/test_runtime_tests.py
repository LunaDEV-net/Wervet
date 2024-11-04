#  Copyright (c) 2024 by https://github.com/LunaDEV-net.
#  all rights reserved

import unittest, sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import runtime_tests
from configuration import configuration as config
from errors import EmptyDataError, EmptyColumnError

# from src import configuration


class test_runtime_tests(unittest.TestCase):
    def test_length_of_data(self):
        self.assertRaises(EmptyDataError, runtime_tests.length_of_data, []) # Should raise an error
        runtime_tests.length_of_data([["a","d","s","f","g","h","h","j","k","l","ö","","",]]) # Should not raise an error
    def test_empty_columns(self):
        empty_test_data = [["" for i in range(20)] for j in range(20)]
        test_data = [["" for i in range(20)] for j in range(20)]
        for index in config.should_not_be_empty_columns:
            for line in test_data:
                line[index] = "something"
        self.assertRaises(EmptyColumnError, runtime_tests.empty_columns, empty_test_data) # Should raise an error
        runtime_tests.empty_columns(test_data)

if __name__ == '__main__':
    unittest.main()
