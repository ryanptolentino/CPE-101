import math
import point


def square_all(l):
    r = []
    for i in range(len(l)):
        r.append(l[i] * l[i])
    return r


def add_n_all(l, n):
    r = [x + n for x in l]
    return r


def distance_all(l):
    r = []
    for i in range(len(l)):
        r.append(math.sqrt((l[i].x * l[i].x) + (l[i].y * l[i].y)))
    return r

