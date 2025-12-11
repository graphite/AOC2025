import sys
import itertools
import functools


def main(stream):
    n = 0
    for l in stream:
        l = l.strip().split()
        goal = int(''.join(['1' if x == '#' else '0' for x in l[0][1:-1][::-1]]), base=2)
        buttons = []
        for b in l[1:-1]:
            buttons.append(sum([2**int(x) for x in b[1:-1].split(',')]))

        found = False
        for i in range(1, len(buttons) + 1):
            for com in itertools.combinations(buttons, i):
                if goal == functools.reduce(lambda x, y: x ^ y, com):
                    found = True
                    n += i
                    break
            if found:
                break

    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
