import unittest
import data
import vector_math
import math
import collisions


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

    def test_point_equals(self):
        pt1 = data.Point(1, 2, 3)
        pt2 = data.Point(1, 2, 3)
        pt3 = data.Point(4, 5, 6)
        self.assertTrue(pt1 == pt2)
        self.assertFalse(pt1 != pt2)
        self.assertTrue(pt1 != pt3)
        self.assertFalse(pt1 == pt3)

    def test_vector_equals(self):
        v1 = data.Vector(1, 2, 3)
        v2 = data.Vector(1, 2, 3)
        v3 = data.Vector(4, 5, 6)
        self.assertTrue(v1 == v2)
        self.assertFalse(v1 != v2)
        self.assertTrue(v1 != v3)
        self.assertFalse(v1 == v3)

    def test_ray_equals(self):
        pt1 = data.Point(1, 2, 3)
        v1 = data.Vector(1, 2, 3)
        pt2 = data.Point(1, 2, 3)
        v2 = data.Vector(1, 2, 3)
        pt3 = data.Point(4, 5, 6)
        v3 = data.Vector(4, 5, 6)
        ray1 = data.Ray(pt1, v1)
        ray2 = data.Ray(pt2, v2)
        ray3 = data.Ray(pt3, v3)
        self.assertTrue(ray1 == ray2)
        self.assertFalse(ray1 != ray2)
        self.assertTrue(ray1 != ray3)
        self.assertFalse(ray1 == ray3)

    def test_sphere_equals(self):
        pt1 = data.Point(1, 2, 3)
        pt2 = data.Point(1, 2, 3)
        pt3 = data.Point(4, 5, 6)
        sphere1 = data.Sphere(pt1, 3.5)
        sphere2 = data.Sphere(pt2, 3.5)
        sphere3 = data.Sphere(pt3, 3.5)
        sphere4 = data.Sphere(pt1, 6.5)
        self.assertTrue(sphere1 == sphere2)
        self.assertFalse(sphere1 != sphere2)
        self.assertTrue(sphere1 != sphere3)
        self.assertFalse(sphere1 == sphere3)
        self.assertTrue(sphere1 != sphere4)
        self.assertFalse(sphere1 == sphere4)

    def test_scale(self):
        v1 = data.Vector(1, 2, 3)
        v2 = data.Vector(1.5, 3, 4.5)
        self.assertEqual(vector_math.scale_vector(v1, 1.5), v2)
        self.assertTrue(vector_math.scale_vector(v1, 1.5) == v2)

    def test_dot_product(self):
        v1 = data.Vector(3, 4, 5)
        v2 = data.Vector(1, 2, 3)
        self.assertEqual(vector_math.dot_vector(v1, v2), 26)

    def test_distance(self):
        v1 = data.Vector(2, 3, 4)
        self.assertAlmostEqual(vector_math.length_vector(v1), 5.385164807)

    def test_normalize(self):
        v1 = data.Vector(1, 2, 3)
        v2 = data.Vector(1/math.sqrt(14), 2/math.sqrt(14), 3/math.sqrt(14))
        self.assertTrue(vector_math.normalize_vector(v1) == v2)
        self.assertTrue(vector_math.length_vector(v2) == 1)

    def test_diff(self):
        p1 = data.Point(5, 6, 7)
        p2 = data.Point(1, 2, 3)
        v1 = data.Vector(4, 4, 4)
        self.assertTrue(vector_math.difference_point(p1, p2) == v1)

    def test_diff_vector(self):
        v1 = data.Vector(5, 6, 7)
        v2 = data.Vector(1, 2, 3)
        v3 = data.Vector(4, 4, 4)
        self.assertTrue(vector_math.difference_vector(v1,v2) == v3)

    def test_translate_point(self):
        p1 = data.Point(9, 0, 1)
        v1 = data.Vector(1, 2, 3)
        p2 = data.Point(10, 2, 4)
        self.assertTrue(vector_math.translate_point(p1, v1) == p2)

    def test_vector_from_to(self):
        p1 = data.Point(1, 2, 3)
        p2 = data.Point(4, 5, 6)
        v1 = data.Vector(3, 3, 3)
        self.assertTrue(vector_math.vector_from_to(p1, p2) == v1)

    def test_sphere_intersection_point(self):
        pt1 = data.Point(-4, -3, -10)
        v1 = data.Vector(-3, -3, -3)
        r1 = data.Ray(pt1, v1)
        pt2 = data.Point(10, 10, 10)
        sphere1 = data.Sphere(pt2, 1)
        self.assertEqual(collisions.sphere_intersection_point(r1, sphere1), None)

    def test_sphere_intersection_point2(self):
        pt1 = data.Point(0, 0, 0)
        v1 = data.Vector(4, 3, 0)
        r1 = data.Ray(pt1, v1)
        pt2 = data.Point(4, 3, 0)
        sphere1 = data.Sphere(pt2, 1)
        intPoint = data.Point(3.2, 2.4, 0)
        self.assertAlmostEqual(collisions.sphere_intersection_point(r1, sphere1).x, intPoint.x)
        self.assertAlmostEqual(collisions.sphere_intersection_point(r1, sphere1).y, intPoint.y)
        self.assertAlmostEqual(collisions.sphere_intersection_point(r1, sphere1).z, intPoint.z)

    def test_sphere_intersection_point3(self):
        pt1 = data.Point(0, 0, 0)
        v1 = data.Vector(8, 6, 0)
        r1 = data.Ray(pt1, v1)
        pt2 = data.Point(8, 6, 0)
        sphere1 = data.Sphere(pt2, 1)
        intPoint = data.Point(7.2, 5.4, 0)
        self.assertAlmostEqual(collisions.sphere_intersection_point(r1, sphere1).x, intPoint.x)
        self.assertAlmostEqual(collisions.sphere_intersection_point(r1, sphere1).y, intPoint.y)
        self.assertAlmostEqual(collisions.sphere_intersection_point(r1, sphere1).z, intPoint.z)

    def test_find_intersection_points(self):
        pt1 = data.Point(0, 0, 0)
        v1 = data.Vector(8, 6, 0)
        r1 = data.Ray(pt1, v1)  # creates ray

        pt2 = data.Point(4, 3, 0)
        sphere1 = data.Sphere(pt2, 1)
        intPoint = data.Point(3.2, 2.4, 0)  # creates sphere and test point

        pt3 = data.Point(10, 10, 10)
        sphere2 = data.Sphere(pt3, 1)  # does not intersect with this sphere instance

        pt4 = data.Point(8, 6, 0)
        sphere3 = data.Sphere(pt4, 1)
        intPoint2 = data.Point(7.2, 5.4, 0)  # creates sphere and test point

        sphere_list = [sphere1, sphere2, sphere3]
        self.assertListEqual(
            collisions.find_intersection_points(sphere_list, r1), [(sphere1, intPoint), (sphere3, intPoint2)])

    def test_sphere_normal_at(self):
        pt1 = data.Point(0, 0, 0)
        sphere = data.Sphere(pt1, 2)
        spherePoint = data.Point(0, 2, 0)
        normalVector = data.Vector(0, 1, 0)
        self.assertEqual(collisions.sphere_normal_at(sphere, spherePoint), normalVector)

    def test_sphere_normal_at2(self):
        pt1 = data.Point(0, 0, 0)
        sphere = data.Sphere(pt1, 1)
        spherePoint = data.Point(1, 0, 0)
        normalVector = data.Vector(1, 0, 0)
        self.assertEqual(collisions.sphere_normal_at(sphere, spherePoint), normalVector)


if __name__ == '__main__':
    unittest.main()
