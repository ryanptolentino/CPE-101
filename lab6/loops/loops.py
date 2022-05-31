def for_version(items):
    result = []
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
    return result


def while_version(items):
    result = []
    i = 0
    while i < len(items):
        reverse = ((len(items)) - 1) - i
        i += 1
        result.append(items[reverse])
    return result
