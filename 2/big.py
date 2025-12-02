import sys

def is_invalid(n):
    s = str(n)
    l = len(s)
    for i in range(1, l // 2 + 1):
        if l % i != 0:
            continue
        g = s[:i]
        for j in range(1, l // i):
            if g != s[j * i : (j + 1) * i]:
                break
        else:
            return True
    return False

def main(stream):
    n = 0
    ranges = stream.read().split(',')
    for r in ranges:
        a, b = [int(x) for x in r.split('-')]
        for i in range(a, b + 1):
            if is_invalid(i):
                n += i
    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
