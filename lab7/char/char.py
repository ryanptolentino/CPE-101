def is_lower_101(letter):
    return 'a' <= letter <= 'z'


def char_rot_13(letter):
    if 'a' <= letter <= 'm':  # for lower case less than m
        return chr(ord(letter) + 13)
    elif 'm' < letter <= 'z': # for lower case greater than m
        return chr(ord(letter) - 13)
    elif 'A' <= letter <= 'M':  # for upper case less than m
        return chr(ord(letter) + 13)
    elif 'M' < letter <= 'Z': # for upper case greater than m
        return chr(ord(letter) - 13)
    else:
        return letter
