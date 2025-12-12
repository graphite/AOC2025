import sys


def main(stream):
    n = 0

    data = stream.read().strip().split('\n\n')
    presents = []
    for present in data[:-1]:
        presents.append(present.count('#'))

    for row in data[-1].split('\n'):
        size, nums = row.split(': ')
        x, y = size.split('x')
        nums = [int(x) for x in nums.split(' ')]
        total = 1
        for i in range(len(nums)):
            total += nums[i] * presents[i]
        if total < int(x) * int(y):
            n += 1

    print(n)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
