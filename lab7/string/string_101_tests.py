import unittest
import string_101


class TestString(unittest.TestCase):
    def test_str_rot_13(self):
        self.assertEqual(string_101.str_rot_13('I like boys'), 'V yvxr oblf')
        pass

    def test_str_rot_13_2(self):
        self.assertEqual(string_101.str_rot_13('cbttref'), 'poggers')
        pass

    def test_str_translate_101(self):
        self.assertEqual(string_101.str_translate_101('Hello', 'l', 'w'), 'Hewwo')
        pass

    def test_str_translate_101_2(self):
        self.assertEqual(string_101.str_translate_101('balls', 's', 'z'), 'ballz')
        pass


if __name__ == '__main__':
    unittest.main()
