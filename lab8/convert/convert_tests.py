import unittest
import convert


class TestConvert(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert.float_default('1', 1), 1.0)
        self.assertEqual(convert.float_default('balls', 0), 0)
        pass


if __name__ == '__main__':
    unittest.main()
