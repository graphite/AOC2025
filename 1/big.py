import sys


def main(stream):
    r = 0
    p = 50
    for l in stream:
        l = l.strip()
        d, n = l[0], int(l[1:])
        fix = 0 if p == 0 and d == 'L' else 1
        p += n * (-1 if d == 'L' else 1)
        if p > 0:
            r += p // 100
        else:
            r += (abs(p) + 100 * fix) // 100
        p %= 100

    print(r)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
