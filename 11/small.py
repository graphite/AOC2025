import sys


def main(stream):
    scheme = {}
    for l in stream:
        start, outs = l.strip().split(':')
        scheme[start] = outs.strip().split()

    n = 0
    outline = ['you']
    while outline:
        current = outline.pop(0)
        for out in scheme[current]:
            if out == 'out':
                n += 1
            else:
                outline.append(out)

    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
