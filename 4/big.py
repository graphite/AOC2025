import sys


def is_valid(x, y, m):
    if x < 0 or y < 0 or x >= len(m) or y >= len(m[0]):
        return False
    return True


def neighbors(x, y, m):
    return [
        (x, y) for (x, y) in (
            (x-1, y), (x+1, y), (x, y-1), (x, y+1),
            (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1),
        ) if is_valid(x, y, m)
    ]


def main(stream):
    layout = [l.strip() for l in stream]
    n = 0
    removed = 100
    while removed != 0:
        removed = 0
        new_layout = [[c for c in layout[k]] for k in range(len(layout))]
        for x in range(len(layout)):
            for y in range(len(layout[0])):
                if layout[x][y] != '@':
                    continue
                a = 0
                for i, j in neighbors(x, y, layout):
                    if layout[i][j] == '@':
                        a += 1
                if a < 4:
                    n += 1
                    removed += 1
                    new_layout[x][y] = '.'
        layout = new_layout
    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
