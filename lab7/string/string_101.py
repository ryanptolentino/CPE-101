from lab7.char.char import *


def str_rot_13(message):
    enc = [char_rot_13(letter) for letter in message]
    return ''.join(enc)


def str_translate_101(message, old, new):
    enc = []
    for letter in message:
        if letter == old:
            enc.append(new)
        else:
            enc.append(letter)
    return ''.join(enc)
