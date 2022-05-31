import unittest
import fold
import point


class TestCases(unittest.TestCase):
    def test_sum(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(fold.sum(numbers), 10)
        pass

    def test_sum_2(self):
        numbers = [2, 5, 3, 1]
        self.assertEqual(fold.sum(numbers), 11)

    def test_index_of_smallest(self):
        numbers = [5, 3, 2, 1, 8]
        self.assertEqual(fold.index_of_smallest(numbers), 3)

    def test_index_of_smallest_2(self):
        numbers = []
        self.assertEqual(fold.index_of_smallest(numbers), -1)

    def test_distance(self):
        pt = point.Point(3, 4)
        self.assertEqual(fold.distance_from_origin(pt), 5)

    def test_nearest_origin(self):
        pt1 = point.Point(3, 4)
        pt2 = point.Point(6, 8)
        pt3 = point.Point(7, 24)
        point_list = [pt3, pt2, pt1]
        self.assertEqual(fold.nearest_origin(point_list), 2)

    def test_nearest_origin2(self):
        point_list = []
        self.assertEqual(fold.nearest_origin(point_list), -1)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
