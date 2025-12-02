import sys

def prev_invalid(n):
    s = str(n)
    if len(s) % 2 == 1:
        return int(''.join(['9'] * (len(s) - 1)))
    s1, s2 = s[:len(s) // 2], s[len(s) // 2 :]
    if int(s1) <= int(s2):
        return int(s1 + s1)
    return int(str(int(s1) - 1) * 2)

def next_invalid(n):
    s = str(n)
    if len(s) % 2 == 1:
        return int(''.join(['1'] + ['0'] * (len(s) // 2)) * 2)
    s1, s2 = s[:len(s) // 2], s[len(s) // 2 :]
    if int(s1) >= int(s2):
        return int(s1 + s1)
    return int(str(int(s1) + 1) * 2)

def main(stream):
    n = 0
    ranges = stream.read().split(',')
    for r in ranges:
        a, b = [int(x) for x in r.split('-')]
        a = next_invalid(a)
        b = prev_invalid(b)
        if b < a:
            continue
        while a <= b:
            n += a
            a = next_invalid(a + 1)
    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
