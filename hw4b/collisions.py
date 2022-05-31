import math
import vector_math


def sphere_intersection_point(ray, sphere):
    dif = vector_math.difference_point(ray.pt, sphere.center)
    a = vector_math.dot_vector(ray.dir, ray.dir)
    b = vector_math.dot_vector(vector_math.scale_vector(dif, 2), ray.dir)
    c = vector_math.dot_vector(dif, dif) - (sphere.radius ** 2)
    d = b ** 2 - (4 * a * c)  # discriminant
    if d < 0:
        return None
    elif d == 0:
        r = (-b) / (2 * a)
        if r >= 0:
            return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, r))
        else:
            return None
    if d > 0:
        t1 = (-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)  # 1st quadratic solution
        t2 = (-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)  # 2nd quadratic solution

        if t1 >= 0 and t2 >= 0:
            return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, min(t1, t2)))
        elif t1 > 0 or t2 > 0:
            return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, max(t1, t2)))


def find_intersection_points(sphere_list, ray):
    r = []
    for i in range(len(sphere_list)):
        c = sphere_intersection_point(ray, sphere_list[i])
        if c is not None:
            r.append((sphere_list[i], c))
    return r


def sphere_normal_at_point(sphere, point):
    normVector = vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
    return normVector
