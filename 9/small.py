import sys


def main(stream):
    red = []
    n = 0
    for l in stream:
        x, y = [int(x) for x in l.strip().split(',')]
        for x1, y1 in red:
            n = max(n, (abs(x - x1) + 1) * (abs(y - y1) + 1))
        red.append((x, y))

    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
