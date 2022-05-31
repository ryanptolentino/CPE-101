import math


def sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


def index_of_smallest(numbers):
    if not numbers:
        return -1
    for i in range(len(numbers)):
        if numbers[i] == min(numbers):
            return i


def distance_from_origin(point):  # creating this function to make the next function cleaner
    return math.sqrt(point.x ** 2 + point.y ** 2)


def nearest_origin(points):
    if not points:
        return -1
    distances = [distance_from_origin(p) for p in points]
    return index_of_smallest(distances)
