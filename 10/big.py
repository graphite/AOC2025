import copy
import itertools
import sys

def simplify(matrix, bmax):
    m, n = len(matrix), len(matrix[0])

    curm = curn = 0
    while curm < m and curn < n:
        # Find non-zero
        for i in range(curm, m):
            if matrix[i][curn] != 0:
                break
        else:
            # Zero column already, move on
            curn += 1
            continue

        if curm != i:
            # Swap cur and i to bring a non-zero to the top
            matrix[curm], matrix[i] = matrix[i], matrix[curm]

        # Nullify the rows below
        for i in range(curm + 1, m):
            if matrix[i][curn] == 0:
                continue

            a, b = matrix[curm][curn], matrix[i][curn]
            for j in range(n):
                matrix[i][j] = matrix[i][j] * a - matrix[curm][j] * b

        curm += 1
        curn += 1

    result = 0
    # Simplify and solve what is possible
    simplified = True
    while simplified:
        simplified = False
        # Drop empty rows and check for unsolvable rows
        for i in range(m - 1, -1, -1):
            if matrix[i][-1] != 0 and matrix[i][:-1].count(0) == n - 1:
                raise ValueError('Unsolvable')
            if any(matrix[i]):
                continue
            simplified = True
            matrix.pop(i)
        m = len(matrix)

        # Solve rows where possible
        for i in range(m):
            if matrix[i][:-1].count(0) != n - 2:
                continue
            # Found a row with a single value
            simplified = True
            for j in range(n - 1):
                if matrix[i][j]:
                    a = matrix[i][j]
                    break
            b = matrix[i][-1]
            if b % a:
                raise ValueError('Non-integer')
            x = b // a
            if x < 0:
                raise ValueError('Negative solution')
            result += x
            bmax.pop(j)
            for row in matrix:
                value = row[j] * x
                row.pop(j)
                row[-1] -= value
            n -= 1
    return result


def solve(matrix, bmax, depth=0):
    try:
        result = simplify(matrix, bmax)
    except ValueError:
        return None

    if not matrix:
        return result

    m, n = len(matrix), len(matrix[0])

    extra = None
    for sol in range(bmax[0] + 1):
        attempt = copy.deepcopy(matrix)
        for row in attempt:
            row[-1] -= row[0] * sol
            row.pop(0)

        steps = solve(attempt, bmax[1:], depth+1)
        if steps:
            if not extra:
                extra = steps + sol
            else:
                extra = min(extra, steps + sol)
    if not extra:
        return None
    result += extra

    return result


def main(stream):
    n = 0

    for l in stream:
        l = l.strip().split()
        goal = [int(x) for x in l[-1][1:-1].split(',')]
        buttons = []
        bmax = []
        for b in l[1:-1]:
            b = [int(x) for x in b[1:-1].split(',')]
            bmax.append(min([goal[i] for i in b]))
            buttons.append([1 if i in b else 0 for i in range(len(goal))])

        matrix = []
        for i in range(len(goal)):
            matrix.append([b[i] for b in buttons])
            matrix[-1].append(goal[i])

        s = solve(matrix, bmax)
        n += s


    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
