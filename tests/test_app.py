import unittest
from app import app  # Replace with your application/module name

class TestApp(unittest.TestCase):
    def test_home_page(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()
