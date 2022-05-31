import unittest
import point
import utility


class TestCases(unittest.TestCase):
    def test_point_one(self):
        pt = point.Point(1, 2)
        self.assertAlmostEqual(pt.x, 1)
        self.assertAlmostEqual(pt.y, 2)

    def test_point_two(self):
        pt = point.Point(-4.7, 19.2)
        self.assertAlmostEqual(pt.x, -4.7)
        self.assertAlmostEqual(pt.y, 19.2)

    def test_equality(self):
        pt1 = point.Point(1, 1)
        pt2 = point.Point(1, 1)
        pt3 = point.Point(2, 3)
        self.assertTrue(pt1 == pt2)
        self.assertFalse(pt1 == pt3)
        pass

    def test_inequality(self):
        pt1 = point.Point(1, 1)
        pt2 = point.Point(1, 1)
        pt3 = point.Point(2, 3)
        self.assertTrue(pt1 != pt3)
        self.assertFalse(pt1 != pt2)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
