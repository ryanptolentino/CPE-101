import unittest
import funcs


class TestCases(unittest.TestCase):
    def test_square(self):
        self.assertEqual(funcs.square(3),9)
        self.assertEqual(funcs.square(4),16)
        pass

    def test_f(self):
        # Add code here
        self.assertEqual(funcs.f(2), 32)
        self.assertEqual(funcs.f(3), 69)
        pass

    def test_g(self):
        self.assertEqual(funcs.g(2,2), 8)
        self.assertEqual(funcs.g(3,3), 18)
        pass

    def test_hypotenuse(self):
        self.assertEqual(funcs.hypotenuse(3, 4), 5)
        self.assertEqual(funcs.hypotenuse(6, 8), 10)
        pass

    def test_is_positive(self):
        self.assertTrue(funcs.is_positive(5))
        self.assertFalse(funcs.is_positive(-5))
        pass

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
