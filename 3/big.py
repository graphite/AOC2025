import sys

def solve(nums, size):
    if size == 1:
        return [max(nums)]
    d1 = max(nums[:-1 * (size - 1)])
    for i in range(len(nums) - size + 1):
        if nums[i] == d1:
            return [d1] + solve(nums[i + 1:], size - 1)

def main(stream):
    n = 0
    for l in stream:
        bs = [int(x) for x in l.strip()]
        n += int(''.join([str(x) for x in solve(bs, 12)]))
    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
