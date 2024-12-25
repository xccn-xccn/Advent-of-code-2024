from sys import argv
from time import perf_counter
from collections import deque, defaultdict
from itertools import groupby
from functools import cache
import re

# issue is when there are 2 options the number of sequences doubles which of course gets very big very quickly
# make best function that takes cx, cy, aim and returns the best sequence 25 steps in
def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def valid_order(seq):
    # seq = ''.join(seq).split('A')
    order = ['^', '<', 'v', '>']

    # print('seq', seq)
    s = [k for k, v in groupby(seq)]
    # print('s', s)
    if len(s) == 2:
        c1, c2 = s
        
        # print(order.index(c1))
        if order[(order.index(c1) + 1) % 4] != c2:
            return False
        
    if len(s) > 2:
        print(seq, s)
        raise Exception
        
    # print('valid')
    return True


def get_paths(cx, cy, seen, sx, sy):
    bag = deque([(cx, cy, [], set([(cx, cy)]))])
    valid = []
    while bag:
        cx, cy, cseq, cseen = bag.popleft()
        if (cx, cy) == (sx, sy):
            break

        for nx, ny, nm in seen[cx, cy]:
            if (nx, ny) in cseen:
                continue
            pseq = cseq.copy()
            pseen = cseen.copy()
            pseen.add((nx, ny))
            pseq.append(nm)
            bag.append((nx, ny, pseq, pseen))

            
            if (nx, ny) == (sx, sy):
                valid.append(pseq)

    if valid:
        # print(valid, [len(x) for x in valid])
        min_len = len(min(valid, key=len))
        valid = [x for x in valid if len(x) == min_len]
        best = min([len(list(groupby(v))) for v in valid])
        valid = [v for v in valid if len(list(groupby(v))) == best]
        # print('valid', valid)
        if len(valid) > 1:
            valid = [v for v in valid if valid_order(v)]
        # print('valid is', valid)

        if len(valid) == 0:
            raise Exception

    # return [x[::-1] + ['A'] for x in valid] if valid else [['A']]
    return valid[0][::-1] + ['A'] if valid else ['A']

@cache
def single(grid, cx, cy, aim):
    sx, sy = cx, cy
    bag = deque([[cx, cy, 0]])
    seen = defaultdict(list)
    conv = {(1, 0): '>', (0, 1): 'v', (-1, 0): '<', (0, -1): '^'}
    best = float('inf')

    while bag:
        
        cx, cy, ct = bag.popleft()
        if grid[cy][cx] == aim:
            # no need TODO
            fx, fy = cx, cy 
            if ct < best:
                best = ct
        if ct > best:
            break

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            px, py = cx + dx, cy + dy
            
            if px < 0 or py < 0 or px >= len(grid[0]) or py >= len(grid) or (cx, cy) in [x[:2] for x in seen[px, py]]:
                continue
            psquare = grid[py][px]
            if psquare == '.':
                continue
            
            if seen[(px, py)] == []:
                bag.append([px, py, ct + 1])
            seen[(px, py)].append((cx, cy, conv[(dx, dy)]))
            

    if not(fx, fy):
        print(grid, aim, sx, sy)
        raise Exception
    
    return fx, fy, get_paths(fx, fy, seen, sx, sy)

@cache
def get_sequence(grids, aim, layer, extra=0):
    # print(layer)
    # if layer >= 10:
    #     print(layer)
    # print(extra)
    if layer == 3 + extra:
        return aim
    if layer == 0:
        cx, cy = 2, 3
        grid = grids[0]
    else:
        cx, cy = 2, 0
        grid = grids[1]

    
    sequence = []
    for a in aim:
        # print(a)
        cx, cy, n_seq = single(grid, cx, cy, a)
        # print(a, n_seq, 'layer', layer)
        # print(len(n_seq))
        # print(n_seq)
        s_seq = get_sequence(grids, ''.join(n_seq), layer+1, extra)
            # print(len(s_seq), 's_seq', s_seq)
        # print('minlen', min_len, 'layer', layer)
        # print('before', sequence, s_seq)
        # print([len(x) for x in s_seq])
        # print(len(sequence))
        # print(s_seq)
        sequence += s_seq
        # print(sequence)
        # print('after', sequence)
        # print('sequence lengths', len(sequence), len(sequence[0]))
        # print(s_seq)

    # print('sequence', sequence, 'layer', layer)
    if layer <= -1:
        print(len(sequence), len(sequence))
    return sequence

def main():
    codes = read_file(get_input_file()).splitlines()

    first_grid = (
        ('7', '8', '9'),
        ('4', '5', '6'),
        ('1', '2', '3'),
        ('.', '0', 'A')
    )

    second_grid = (
        ('.', '^', 'A'),
        ('<', 'v', '>')
    )

    grids = (first_grid, second_grid)

    d_lengths = {}
    for d in '^v<>A':
        d_lengths[d] = get_sequence(grids, d, 1, extra=2)

    # print(d_lengths)
    count = 0
    for code in codes: 
        sequence = get_sequence(grids, code, 0)
        # print(sequence, len(sequence[0]), [len(x) for x in sequence])
        # s_count = sum([len(d_lengths[x]) for x in sequence])
        # count += s_count * int(list(re.findall('\d+', code))[0])
        count += len(sequence) * int(list(re.findall('\d+', code))[0])

    print(len(str(count)))
    return count
if __name__ == "__main__":
    start = perf_counter()
    print('thestart')
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')

# 423973575795644 (15d) too high 65825838402202 (14d) too low?