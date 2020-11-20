import unittest
import datetime
import requests
import json
class TestMethods(unittest.TestCase):
    def test_symbol(self):
        self.assertTrue('userInput1'.isupper())
        self.assertTrue('userInput1'.isalnum())
    def test_chart(self):
        self.assertTrue('userInput2' === 1 || 'userInput2' === 2)
    def test_series(self):
        self.assertTrue('userInput3'.isnum())
        self.assertTrue('userInput3' === 1 || 'userInput3' === 2 || 'userInput3' === 3 || 'userInput3' === 4)
    def test_start(self):
        self.assertTrue(datetime.datetime.strptime('userInput4', '%Y-%m-d'))
    def test_end(self):
        self.assertTrue(datetime.datetime.strptime('userInput5', '%Y-%m-d'))
