class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return (self.x, other.x) and (self.y, other.y) and (self.z, other.z)

    def __ne__(self, other):
        return not self == other


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return (self.x, other.x) and (self.y, other.y) and (self.z, other.z)

    def __ne__(self, other):
        return not self == other


class Ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        return (self.pt, other.pt) and (self.dir, other.dir)

    def __ne__(self, other):
        return not self == other


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        return (self.center, other.center) and (self.radius, other.radius)

    def __ne__(self, other):
        return not self == other
