import sys

def main(stream):
    rays = set()
    n = 0
    for l in stream:
        l = l.strip()
        if not rays:
            if 'S' not in l:
                continue
            else:
                rays.add(l.find('S'))
        else:
            new_rays = set()
            for r in rays:
                if l[r] == '.':
                    new_rays.add(r)
                else:
                    n += 1
                    if r > 0:
                        new_rays.add(r - 1)
                    if r < len(l) - 1:
                        new_rays.add(r + 1)
            rays = new_rays

    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
