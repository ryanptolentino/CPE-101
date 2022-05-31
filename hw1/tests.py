import unittest
import data


class TestData(unittest.TestCase):
    def test_point_1(self):
        pt1 = data.Point(1, 2, 3)
        self.assertEqual(pt1.x, 1)
        self.assertEqual(pt1.y, 2)
        self.assertEqual(pt1.z, 3)

    def test_point_2(self):
        pt2 = data.Point(4, 5, 6)
        self.assertEqual(pt2.x, 4)
        self.assertEqual(pt2.y, 5)
        self.assertEqual(pt2.z, 6)

    def test_vector_1(self):
        v1 = data.Vector(1, 2, 3)
        self.assertEqual(v1.x, 1)
        self.assertEqual(v1.y, 2)
        self.assertEqual(v1.z, 3)

    def test_vector_2(self):
        v2 = data.Vector(4, 5, 6)
        self.assertEqual(v2.x, 4)
        self.assertEqual(v2.y, 5)
        self.assertEqual(v2.z, 6)

    def test_ray_1(self):
        pt1 = data.Point(1, 2, 3)
        v1 = data.Point(1, 2, 3)
        ray1 = data.Ray(pt1, v1)
        self.assertTrue(ray1.pt == pt1)
        self.assertTrue(ray1.dir == v1)

    def test_ray_2(self):
        pt2 = data.Point(4, 5, 6)
        v2 = data.Point(4, 5, 6)
        ray2 = data.Ray(pt2, v2)
        self.assertTrue(ray2.pt == pt2)
        self.assertEqual(ray2.dir, v2)

    def test_sphere_1(self):
        pt1 = data.Point(1, 2, 3)
        sphere1 = data.Sphere(pt1, 3.5)
        self.assertTrue(sphere1.center == pt1)
        self.assertEqual(sphere1.radius, 3.5)

    def test_sphere_2(self):
        pt2 = data.Point(4, 5, 6)
        sphere2 = data.Sphere(pt2, 4.5)
        self.assertTrue(sphere2.center == pt2)
        self.assertEqual(sphere2.radius, 4.5)


if __name__ == '__main__':
    unittest.main()
