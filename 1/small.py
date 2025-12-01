import sys


def main(stream):
    r = 0
    p = 50
    for l in stream:
        l = l.strip()
        d, n = l[0], int(l[1:])
        p += n * (-1 if d == 'L' else 1)
        p %= 100
        if not p:
            r += 1

    print(r)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
