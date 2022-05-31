import sys

try:
    text = open(sys.argv[1], 'r')
except IndexError:
    print('data.txt not found :(')
    sys.exit()

for args in text:
    try:
        split = args.split()
        print(split, float(split[0]) + float(split[1]))
    except ValueError:
        print('Cannot convert string to float :(')
    except IndexError:
        print('Missing Value :(')

