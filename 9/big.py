#import line_profiler
from collections import defaultdict

import sys

def nxt(n, ns):
    for i in range(len(ns)):
        if ns[i] == n:
            return ns[i+1] if i < len(ns) else n + 1
        elif ns[i] > n:
            return ns[i]
    return n + 1

#@line_profiler.profile
def main(stream):
    red = []
    for l in stream:
        red.append([int(x) for x in l.strip().split(',')])

    intervals = []
    for i in range(len(red) - 1):
        intervals.append((red[i], red[i+1]))

    intervals.append((red[-1], red[0]))
    vint = defaultdict(list)
    hint = defaultdict(list)
    for i in intervals:
        x1, y1 = i[0]
        x2, y2 = i[1]
        if x1 == x2:
            vint[x1].append((y1, y2))
        else:
            hint[y1].append((x1, x2))

    for x in vint.values():
        x.sort()

    for x in hint.values():
        x.sort()

    xs = sorted([k for k in vint.keys()])
    ys = sorted([k for k in hint.keys()])

    n = 0
    for i in range(len(red)):
        for j in range(i + 1, len(red)):
            x1, y1 = red[i]
            x2, y2 = red[j]
            max_x, max_y, min_x, min_y = max(x1, x2), max(y1, y2), min(x1, x2), min(y1, y2)
            valid = True
            for row in y1, y2:
                if not valid:
                    break
                p = 0
                inside = False
                direction = 0
                while valid and p < max_x:
                    moveon = False
                    if p in vint:
                        for v1, v2 in vint[p]:
                            if min(v1, v2) <= row <= max(v1, v2):
                                new_direction = v2 - v1
                                if direction == 0:
                                    inside = True
                                elif new_direction * direction < 0:
                                    inside = not inside
                                direction = new_direction
                                p += 1
                                moveon = True
                                break
                    if moveon:
                        continue

                    if row in hint:
                        for h1, h2 in hint[row]:
                            if min(h1, h2) <= p <= max(h1, h2):
                                p = max(h1, h2) 
                                moveon = True
                                break
                    if moveon:
                        continue

                    if min_x <= p <= max_x and not inside:
                        valid = False
                        break
                    p = nxt(p, xs)

            for column in x1, x2:
                if not valid:
                    break
                p = 0
                inside = False
                direction = 0
                while valid and p < max_y:
                    moveon = False
                    if p in hint:
                        for h1, h2 in hint[p]:
                            if min(h1, h2) <= column <= max(h1, h2):
                                new_direction = h2 - h1
                                if direction == 0:
                                    inside = True
                                elif new_direction * direction < 0:
                                    inside = not inside
                                direction = new_direction
                                p += 1
                                moveon = True
                                break
                    if moveon:
                        continue

                    if column in vint:
                        for v1, v2 in vint[column]:
                            if min(v1, v2) <= p <= max(v1, v2):
                                p = max(v1, v2) 
                                moveon = True
                                break
                    if moveon:
                        continue

                    if min_y <= p <= max_y and not inside:
                        valid = False
                        break
                    p = nxt(p, ys)


            if valid:
                n = max(n, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
