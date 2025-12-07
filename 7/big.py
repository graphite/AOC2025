import sys


def count(x, y, layout, cache):
    if x == len(layout) - 1:
        return 1
    if (x, y) not in cache:
        if layout[x][y] == '.':
            cache[(x, y)] = count(x + 1, y, layout, cache)
        else:
            cache[(x, y)] = 0
            if y > 0:
                cache[(x, y)] += count(x + 1, y - 1, layout, cache)
            if y < len(layout[0]) - 1:
                cache[(x, y)] += count(x + 1, y + 1, layout, cache)
    return cache[(x, y)]


def main(stream):
    layout = [l.strip() for l in stream]
    cache = dict()
    print(count(0, layout[0].find('S'), layout, cache))
    

if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
