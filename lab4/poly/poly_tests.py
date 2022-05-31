import unittest
import poly


class TestPoly(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_poly(self):
        poly1 = [1.5, 2.5, 3.5]
        poly2 = [2, 3, 4]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.5, 5.5, 7.5])

    def test_poly_add2(self):
        poly1 = [1.5, 2.5, 3.5]
        poly2 = [.5, 1.5, 2.5]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [2, 4, 6])

    def test_poly_mult(self):
        poly1 = [3, 2, 1]
        poly2 = [1, 1, 3]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3, 5, 12, 7, 3])

    def test_poly_mult2(self):
        poly1 = [4, 6, 8]
        poly2 = [3, 7, 9]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [12, 46, 102, 110, 72])


if __name__ == '__main__':
    unittest.main()
