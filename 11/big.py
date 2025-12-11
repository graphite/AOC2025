import sys
from collections import defaultdict


def solve(fr, to, ins, scheme):
    unreachable = set([x for x in ins])
    pending = [to]
    unreachable.remove(to)
    while pending:
        cur = pending.pop(0)
        for node in ins[cur]:
            if node in unreachable:
                pending.append(node)
                unreachable.remove(node)
    solved = {to: 1}
    for u in unreachable:
        solved[u] = 0

    outline = set([x for x in ins[to]])
    while outline:
        new_outline = set()
        new_outline.update(outline)
        found = False
        for o in outline:
            if all([x in solved for x in scheme[o]]):
                found = True
                solved[o] = sum([solved[x] for x in scheme[o]])
                new_outline.update(ins[o])
        if not found:
            return None
        for o in solved:
            if o in new_outline:
                new_outline.remove(o)
        outline = new_outline
        if fr in solved:
            return solved[fr]

    return None


def main(stream):
    scheme = {}
    ins = defaultdict(list)
    for l in stream:
        start, outs = l.strip().split(':')
        outs = outs.strip().split()
        scheme[start] = outs
        for out in outs:
            ins[out].append(start)

    dac_out = solve('dac', 'out', ins, scheme)
    fft_dac = solve('fft', 'dac', ins, scheme)
    svr_fft = solve('svr', 'fft', ins, scheme)
    print(svr_fft * fft_dac * dac_out)


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else 'sample.txt'
    main(open(infile))
