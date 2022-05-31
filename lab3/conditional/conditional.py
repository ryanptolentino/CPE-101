def max_101(x, y):
    if x > y:
        return x
    else:
        return y


def max_of_three(x, y, z):
    if max_101(x, y) > z:
        return max_101(x, y)
    else:
        return z


def rental_late_fee(days):
    if 0 <= days < 9:
        return 0
    elif 9 <= days < 15:
        return 5
    elif 15 <= days < 24:
        return 7
    elif days == 24:
        return 19
    else:
        return 100
