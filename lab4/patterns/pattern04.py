import driver


def letter(row, col):
    if 1 < row < 5 and 2 < col < 7:
        return 'M'
    else:
        return 'S'


if __name__ == '__main__':
    driver.comparePatterns(letter)