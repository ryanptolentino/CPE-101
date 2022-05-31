import data
import vector_math
import collisions


def cast_ray(ray, sphere_list):
    test = collisions.find_intersection_points(sphere_list, ray)
    if test:
        return True


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color):
    y_interval = (max_y - min_y) / height
    x_interval = (max_x - min_x) / width

    for i in range(height, 0, -1):
        for j in range(width):
            x = min_x + j * x_interval
            y = min_y + i * y_interval
            p = data.Point(x, y, 0)
            r = data.Ray(eye_point, vector_math.vector_from_to(eye_point, p))
            if cast_ray(r, sphere_list) is True:
                print('0 0 0')
            else:
                print('255 255 255')
