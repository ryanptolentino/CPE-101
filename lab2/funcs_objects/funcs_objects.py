import math


def distance(pointa, pointb):
    return math.sqrt(((pointb.x-pointa.x)*(pointb.x-pointa.x))+((pointb.y-pointa.y)*(pointb.y-pointa.y)))

def circle_overlap(circlea, circleb):
    radiisum = circlea.radius + circleb.radius
    return distance(circlea.center, circleb.center) < radiisum