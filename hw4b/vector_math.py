import data
import math


def scale_vector(vector, scalar):
    x = vector.x * scalar
    y = vector.y * scalar
    z = vector.z * scalar
    nvector = data.Vector(x, y, z)
    return nvector


def dot_vector(vector1, vector2):
    return (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)


def length_vector(vector):
    return math.sqrt(vector.x*vector.x + vector.y*vector.y + vector.z*vector.z)


def normalize_vector(vector):
    normVector = scale_vector(vector, 1/length_vector(vector))
    return normVector


def difference_point(point1, point2):
    diffVector = data.Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)
    return diffVector


def difference_vector(vector1, vector2):
    diffVector = data.Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)
    return diffVector


def translate_point(point, vector):
    newPoint = data.Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)
    return newPoint


def vector_from_to(from_point, to_point):
    vector = data.Vector(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)
    return vector
