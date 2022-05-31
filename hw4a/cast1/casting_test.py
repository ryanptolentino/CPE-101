from data import *
from cast import *
from vector_math import *
import math
import utility

print('P3')
print('512 384')
print('255')
min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 512
height = 384
eye_point = data.Point(0, 0, -14)
sphere1 = data.Sphere(data.Point(1, 1, 0), 2, data.Color(0, 0, 255), .2)
sphere2 = data.Sphere(data.Point(.5, 1.5, -3), .5, data.Color(255, 0, 0), .4)
sphere_list = [sphere1, sphere2]
color = data.Color(255, 255, 255)

cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color)
