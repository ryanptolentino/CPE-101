import unittest
import logic


class TestCases(unittest.TestCase):
    def test_case(self):
        self.assertTrue(logic.is_even(6))
        self.assertFalse(logic.is_even(5))
        pass

    def test_interval(self):
        self.assertTrue(logic.in_an_interval(3))
        self.assertTrue(logic.in_an_interval(48))
        self.assertTrue(logic.in_an_interval(19))
        self.assertTrue(logic.in_an_interval(102))
        self.assertFalse(logic.in_an_interval(10))
        pass

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
