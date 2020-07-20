import unittest
import Ydx_translate


class TestYT(unittest.TestCase):

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

    def test_negative(self):
        self.assertRaises(TypeError, Ydx_translate.translate_text("Привет") != "Hello")

    def test_positive(self):
        self.assertTrue(Ydx_translate.translate_text("Привет"), "Hello")


if __name__ == "__main__":

    unittest.main()
