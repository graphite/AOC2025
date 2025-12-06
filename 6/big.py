import sys

def main(stream):
    inp = stream.read().split('\n')
    transposed = [[] for _ in range(len(inp[0]))]
    for l in inp:
        i = 0
        for c in l:
            transposed[i].append(c)
            i += 1
    transposed = [''.join(x).strip() for x in transposed]

    r = 0
    i = 0
    n = action = None
    while i < len(transposed):
        if not action:
            action = transposed[i][-1]
            n = int(transposed[i][:-1])
        elif not transposed[i]:
            r += n
            n = action = None
        else:
            if action == '+':
                n += int(transposed[i])
            else:
                n *= int(transposed[i])
        i += 1
    r += n

    print(r)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
