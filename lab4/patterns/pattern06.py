import driver


def letter(row, col):
    if row == col or row == 6 - col:
        return 'X'
    else:
        return 'O'


if __name__ == '__main__':
    driver.comparePatterns(letter)