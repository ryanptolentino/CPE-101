import unittest
import filter
import point


class TestCases(unittest.TestCase):
    def test_are_positive(self):
        list1 = [1, -3, 2, 6, -7]
        result = [1, 2, 6]
        self.assertListEqual(filter.are_positive(list1), result)
        pass

    def test_are_greater_than(self):
        numbers = [1, -3, 2, 6, -7]
        result = [2, 6]
        self.assertListEqual(filter.are_greater_than(numbers, 1), result)
        pass

    def test_are_greater_than2(self):
        numbers = [1, -3, 2, 6, -7]
        result = [2, 6]
        self.assertListEqual(filter.are_greater_than2(numbers, 1), result)
        pass

    def test_are_in_first_quadrant(self):
        pt1 = point.Point(1, 3)
        pt2 = point.Point(-2, 4)
        pt3 = point.Point(-3, -4)
        pt4 = point.Point(3, -2)
        pt5 = point.Point(3, 6)
        points = [pt1, pt2, pt3, pt4, pt5]
        result = [pt1, pt5]
        self.assertListEqual(filter.are_in_first_quadrant(points), result)


if __name__ == '__main__':
    unittest.main()
