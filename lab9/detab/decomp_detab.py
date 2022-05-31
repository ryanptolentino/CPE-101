import sys


def main(argv):
    error(argv)
    inp = in_file(argv)
    out = out_file(argv)
    tab(inp, out)
    inp.close()
    out.close()


def error(arg):
    if len(arg) < 2:
        print >> sys.stderr, "file name missing"
        sys.exit()


def in_file(arg):
    try:
        return open(sys.argv[1], 'r')
    except IOError as e:
        print >> sys.stderr, e
        sys.exit()


def out_file(arg):
    try:
        return open('decomp', 'w')
    except IOError as e:
        print >> sys.stderr, e
        sys.exit()


def tab(inp, out):
    char_count = 0
    c = inp.read(1)
    while c:
        if c == '\t':
            num_spaces = 8 - (char_count % 8)
            for i in range(num_spaces):
                out.write(' ')
            char_count += num_spaces
        elif c == '\n':
            out.write('\n')
            char_count = 0
        else:
            out.write(c)
            char_count += 1
        c = inp.read(1)


if __name__ == "__main__":
    main(sys.argv)
