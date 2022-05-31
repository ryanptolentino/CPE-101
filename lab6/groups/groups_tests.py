import unittest
import groups


class TestGroups(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_groups(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertListEqual(groups.groups_of_three(numbers), result)

    def test_groups2(self):
        numbers = [1, 2, 3, 4, 5, 6, 7]
        result = [[1, 2, 3], [4, 5, 6], [7]]
        self.assertListEqual(groups.groups_of_three(numbers), result)
    # Add tests here


if __name__ == '__main__':
    unittest.main()
