import sys

try:  # opens file
    text = open(sys.argv[1], 'r')
except IndexError:  # if file doesn't exist print that it doesn't
    print('file does not exist')
    sys.exit()

col = int(sys.argv[2])


def column(file, c):
    vertical = []  # list of specified column
    for args in file:
        try:
            split = args.split()
            vertical.append(split[c])
        except IndexError:  # if not enough values in column move on
            break
    if not vertical:  # if list is empty that means the column does not exist
        print('no worky: column does not exist')
        sys.exit()
    return vertical


def tally(l):  # converts list to float then adds (if a string then return error message)
    r = []
    for i in l:
        try:
            r.append(float(i))
        except ValueError:
            print(i, 'cannot be converted to a number')
    add = sum(r)
    print(add)


spec = column(text, col)
tally(spec)
