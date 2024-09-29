import unittest
from app import main_function

class TestApp(unittest.TestCase):
    def test_main_function(self):
        result = main_function()
        self.assertEqual(result, "Hello from the main function")

if __name__ == '__main__':
    unittest.main()
