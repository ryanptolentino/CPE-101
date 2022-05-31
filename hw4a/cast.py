import data
from vector_math import *
import collisions


def cast_ray(ray, sphere_list, color):
    test = collisions.find_intersection_points(sphere_list, ray)
    int_list = [tpl[1] for tpl in test]
    distances = []

    if test:
        for p in range(len(int_list)):
            distances.append(length_vector(difference_point(ray.pt, int_list[p])))

        near = test[distances.index(min(distances))][0]
        return str(near.color.r * near.finish) + ' ' + str(
            near.color.g * near.finish) + ' ' + str(near.color.b * near.finish)

    else:
        return str(color.r) + ' ' + str(color.g) + ' ' + str(color.b)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color):
    y_interval = (max_y - min_y) / height
    x_interval = (max_x - min_x) / width

    for i in range(height, 0, -1):
        for j in range(width):
            x = min_x + j * x_interval
            y = min_y + i * y_interval
            p = data.Point(x, y, 0)
            r = data.Ray(eye_point, vector_from_to(eye_point, p))
            print(cast_ray(r, sphere_list, color))
