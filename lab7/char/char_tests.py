import unittest
import char


class TestChar(unittest.TestCase):
    def test_lower(self):
        self.assertTrue(char.is_lower_101('a'))
        pass

    def test_lower2(self):
        self.assertFalse(char.is_lower_101('A'))
        pass

    def test_char_rot_13(self):
        self.assertEqual(char.char_rot_13('b'), 'o')

    def test_char_rot13_2(self):
        self.assertEqual(char.char_rot_13('s'), 'f')

    def test_char_rot13_3(self):  # tests for spaces
        self.assertEqual(char.char_rot_13(' '), ' ')


if __name__ == '__main__':
    unittest.main()
