def are_positive(l):
    r = [l[i] for i in range(len(l)) if l[i] > 0]
    return r


def are_greater_than(l, n):
    r = []
    for g in l:
        if g > n:
            r.append(g)
    return r


def are_greater_than2(l, n):
    r = [g for g in l if g > n]
    return r

def are_in_first_quadrant(l):
    r = []
    for i in range(len(l)):
        if l[i].x > 0 and l[i].y > 0:
            r.append(l[i])
    return r
