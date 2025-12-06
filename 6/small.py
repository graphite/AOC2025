import math
import sys
from collections import defaultdict

def main(stream):
    problems = defaultdict(list)
    for l in stream:
        if l[0] == '+' or l[0] == '*':
            break
        i = 0
        for n in l.strip().split():
            problems[i].append(int(n))
            i += 1

    r = 0
    i = 0
    for s in l.strip().split():
        if s == '+':
            r += sum(problems[i])
        else:
            r += math.prod(problems[i])
        i += 1
    print(r)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
