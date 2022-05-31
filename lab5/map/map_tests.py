import math
import unittest
import map
import point


class TestCases(unittest.TestCase):
    def test_square_all(self):
        inputList = [4, 6, 2, 8]
        result = [16, 36, 4, 64]
        self.assertListEqual(map.square_all(inputList), result)
        pass

    def test_add_n_all(self):
        inputList1 = [4, 5, 3, 2]
        result = [7, 8, 6, 5]
        self.assertListEqual(map.add_n_all(inputList1, 3), result)
        pass

    def test_distance_all(self):
        pt1 = point.Point(2, 2)
        pt2 = point.Point(3, 3)
        pt3 = point.Point(4, 4)
        points = [pt1, pt2, pt3]
        result = [2 * math.sqrt(2), 4.242640687119285, 4 * math.sqrt(2)]
        self.assertListEqual(map.distance_all(points), result)


if __name__ == '__main__':
    unittest.main()
