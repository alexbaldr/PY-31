import unittest
import helper
from unittest.mock import patch


class TestMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        print("==========")

    def setUp(self):
        print(self.shortDescription())

    def tearDown(self):
        print(self.shortDescription())

    def test_get_info(self):
        self.assertNotIn('333', helper.directories['3'])
        with patch("helper.input", side_effect=["333", "3", "Vi", '3']):
            helper.get_adding(helper.directories, helper.documents)
            self.assertIn('333', helper.directories['3'])

    def test_raise(self):
        self.assertRaises(TypeError, helper.get_names())


if __name__ == '__main__':

    unittest.main()
