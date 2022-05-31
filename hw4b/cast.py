import collisions
import data
import vector_math


def cast_ray(ray, sphere_list, ambient, light):
    intersect = collisions.find_intersection_points(sphere_list, ray)
    if not intersect:
        return data.Color(1.0, 1.0, 1.0)
    else:
        nearest = 0
        for i in range(len(intersect)):
            if vector_math.length_vector(
                    vector_math.vector_from_to(ray.pt, intersect[i][1])) < vector_math.length_vector(
                    vector_math.vector_from_to(ray.pt, intersect[nearest][1])):
                nearest = i
            r = intersect[nearest][0].color.r * ambient.r * intersect[nearest][0].finish.ambient
            g = intersect[nearest][0].color.g * ambient.g * intersect[nearest][0].finish.ambient
            b = intersect[nearest][0].color.b * ambient.b * intersect[nearest][0].finish.ambient

        n = collisions.sphere_normal_at_point(intersect[nearest][0], intersect[nearest][1])
        pe = vector_math.translate_point(intersect[nearest][1], vector_math.scale_vector(n, 0.01))
        l_dir = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.pt))
        visible = vector_math.dot_vector(l_dir, collisions.sphere_normal_at_point(intersect[nearest][0], pe))
        ray_col = data.Ray(pe, vector_math.vector_from_to(pe, light.pt))

        if visible > 0:
            intersect1 = collisions.find_intersection_points(sphere_list, ray_col)
            if not intersect1:
                r += light.color.r * visible * intersect[nearest][0].finish.diffuse * intersect[nearest][0].color.r
                g += light.color.g * visible * intersect[nearest][0].finish.diffuse * intersect[nearest][0].color.g
                b += light.color.b * visible * intersect[nearest][0].finish.diffuse * intersect[nearest][0].color.b
        return data.Color(r, g, b)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light):
    step_x = (max_x - min_x) / width
    step_y = (max_y - min_y) / height

    for i in range(height):
        for j in range(width):
            x = min_x + j * step_x
            y = max_y - i * step_y

            dir = vector_math.vector_from_to(eye_point, data.Point(x, y, 0))
            ray = data.Ray(eye_point, dir)
            check = cast_ray(ray, sphere_list, ambient, light)

            r = scale(check.r)
            print(r)

            g = scale(check.g)
            print(g)

            b = scale(check.b)
            print(b)

            # if 1 <= x <= 1.1 and 1.4 <= y <= 1.5:
            #     print(x, y)

def scale(check):
    result = int(check * 255)
    if result > 255:
        result = 255
    return result