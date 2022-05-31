from data import *
from cast import *
from vector_math import *
import math
import utility

print("P3")
print("512 384")
print("255")

min_x = -10.0
max_x = 10.0
min_y = -7.5
max_y = 7.5
width = 512
height = 384
eye_point = Point(0.0, 0.0, -14.0)
ambient = Color(1.0, 1.0, 1.0)
light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
finish1 = Finish(0.2, 0.4, 0.5, 0.05)
finish2 = Finish(0.4, 0.4, 0.5, 0.05)
sphere1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), finish1)
sphere2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), finish2)
sphere_list = [sphere1, sphere2]
cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light)
