import sys


def main(stream):
    ranges = []
    for r in stream:
        if not r.strip():
            break
        a, b = [int(x) for x in r.strip().split('-')]
        ranges.append([a, b])

    ranges.sort()
    merged = []
    i = 0
    while i < len(ranges):
        a, b = ranges[i]
        i += 1
        while i < len(ranges):
            if b < ranges[i][0]:
                merged.append([a, b])
                a = b = None
                break
            b = max(b, ranges[i][1])
            i += 1
        if a:
            merged.append([a, b])
        
    n = 0
    for x in stream:
        x = int(x.strip())
        for a, b in merged:
            if x >= a and x <= b:
                n += 1
                break
            if x < a:
                break
    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
