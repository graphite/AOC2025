import sys


class Circuit:
    def __init__(self, num, boxes):
        self.boxes = set(boxes)
        self.num = num

    def merge(self, other):
        self.boxes = self.boxes.union(other.boxes)


class Box:
    def __init__(self, x, y, z, c):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = c

    def distance(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2

    def __hash__(self):
        return hash((self.x, self.y, self.z))


def main(stream):
    distances = []
    boxes = []
    circuits = {}
    i = 0
    for l in stream:
        c = Circuit(i, [])
        circuits[i] = c
        x, y, z = [int(x) for x in l.strip().split(',')]
        b = Box(x, y, z, c)
        c.boxes.add(b)
        for b1 in boxes:
            distances.append((b.distance(b1), b, b1))
        boxes.append(b)
        i += 1

    distances.sort(key=lambda x: x[0], reverse=True)
    for _ in range(1000):
        _, b1, b2 = distances.pop()
        c1, c2 = b1.circuit, b2.circuit
        if c1.num == c2.num:
            continue
        for box in c2.boxes:
            box.circuit = c1
        c1.merge(c2)
        del circuits[c2.num]

    circuits = sorted(circuits.values(), key=lambda x: len(x.boxes), reverse=True)
    n = 1
    for c in circuits[:3]:
        n *= len(c.boxes)

    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
