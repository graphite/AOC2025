import sys

def main(stream):
    n = 0
    for l in stream:
        bs = [int(x) for x in l.strip()]
        d1 = max(bs[:-1])
        for i in range(len(bs) - 1):
            if bs[i] == d1:
                n += d1 * 10 + max(bs[i + 1:])
                break
    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
