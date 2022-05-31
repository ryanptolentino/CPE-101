import driver


def letter(row, col):
    if (3 < col < 10 and 1 < row < 4) or (3 < col < 7 and 3 < row < 6):
        return 'Z'
    elif 6 < col < 10 and 3 < row < 6:
        return 'X'
    elif (9 < col < 13 and 3 < row < 7) or (6 < col < 10 and row == 6):
        return 'B'
    else:
        return 'T'


if __name__ == '__main__':
    driver.comparePatterns(letter)