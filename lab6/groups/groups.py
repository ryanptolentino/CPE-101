def groups_of_three(sep):
    r = []
    s = 0
    e = 3
    while s < len(sep):
        r.append(sep[s:e])
        s += 3
        e += 3
    return r
