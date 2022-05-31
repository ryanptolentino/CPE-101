from data import *
from vector_math import *
from collisions import *


def cast_ray(ray, sphere_list, ambient, light, point):
    c = find_intersection_points(sphere_list, ray)
    if not c:
        return Color(1.0, 1.0, 1.0)
    else:
        nearest = 0
        for i in range(len(c)):
            if length_vector(vector_from_to(ray.pt, c[i][1])) < length_vector(vector_from_to(ray.pt, c[nearest][1])):
                nearest = i

            r = c[nearest][0].color.r * ambient.r * c[nearest][0].finish.ambient
            g = c[nearest][0].color.g * ambient.g * c[nearest][0].finish.ambient
            b = c[nearest][0].color.b * ambient.b * c[nearest][0].finish.ambient

        n = sphere_normal_at_point(c[nearest][0], c[nearest][1])
        Pe = translate_point(c[nearest][1], scale_vector(n, 0.01))
        light_dir = normalize_vector(vector_from_to(Pe, light.pt))
        visible = dot_vector(light_dir, sphere_normal_at_point(c[nearest][0], Pe))
        ray_col = Ray(Pe, vector_from_to(Pe, light.pt))

        reflection = difference_vector(light_dir, scale_vector(n, 2 * visible))
        v_dir = normalize_vector(vector_from_to(point, Pe))
        spec = dot_vector(reflection, v_dir)

        sphere = c[nearest][0]
        if visible > 0:
            c1 = find_intersection_points(sphere_list, ray_col)
            if not c1:
                r += light.color.r * visible * sphere.finish.diffuse * sphere.color.r
                b += light.color.b * visible * sphere.finish.diffuse * sphere.color.b
                g += light.color.g * visible * sphere.finish.diffuse * sphere.color.g

        if spec > 0:
            r += light.color.r * sphere.finish.specular * (spec ** (1 / sphere.finish.roughness))
            g += light.color.g * sphere.finish.specular * (spec ** (1 / sphere.finish.roughness))
            b += light.color.b * sphere.finish.specular * (spec ** (1 / sphere.finish.roughness))

        return Color(r, g, b)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light):
    w_interval = (max_x - min_x) / float(width)
    h_interval = (max_y - min_y) / float(height)

    for i2 in range(height):
        y = max_y - (i2 * h_interval)
        for i in range(width):
            x = min_x + (i * w_interval)

            dir = vector_from_to(eye_point, Point(x, y, 0))
            ray = Ray(eye_point, dir)
            check = cast_ray(ray, sphere_list, ambient, light, eye_point)

            r = scaler(check.r)
            g = scaler(check.g)
            b = scaler(check.b)

            print(r, g, b)


def scaler(check):
    result = int(check * 255)
    if result > 255:
        result = 255
    return result
