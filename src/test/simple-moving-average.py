import unittest
from src import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.test_run(), )


if __name__ == '__main__':
    unittest.main()
