import unittest
from funcs_objects import distance, circle_overlap
import objects

# creating points
point1 = objects.point(1, 1)
point2 = objects.point(4, 5)
point3 = objects.point(0, 0)

# creating circles
circle1 = objects.circle(point1, 3)
circle2 = objects.circle(point2, 3)
circle3 = objects.circle(point2, 1)
circle4 = objects.circle(point3, 1)


# testing cases for functions for objects
class TestCases(unittest.TestCase):

    def test_cases_distance(self):
        self.assertEqual(distance(point1, point2), 5)
        self.assertEqual(distance(point1, point1), 0)
        pass

    def test_cases_overlap(self):
        self.assertTrue(circle_overlap(circle1, circle2))
        self.assertFalse(circle_overlap(circle1, circle3))
        self.assertFalse(circle_overlap(circle4, circle3))
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()