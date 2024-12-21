from sys import argv
from time import perf_counter
from collections import deque
import re


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def get_path(cx, cy, seen):
    sequence = []
    while seen[cx, cy] != None:
        sequence.append(seen[cx, cy][2])
        cx, cy = seen[(cx, cy)][:2]

    return sequence[::-1] + ['A']
def single(grid, cx, cy, aim):
    bag = deque([[cx, cy, 0]])
    seen = {(cx, cy): None}
    conv = {(1, 0): '>', (0, 1): 'v', (-1, 0): '<', (0, -1): '^'}
    best = float('inf')
    poss = []

    while bag:
        cx, cy, ct = bag.popleft()
        if grid[cy][cx] == aim:
            if ct < best:

                poss = [(cx, cy)]
                best = ct
            elif ct == best:
                poss.append((cx, cy))
            else:
                break
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            px, py = cx + dx, cy + dy
            
            if px < 0 or py < 0 or px >= len(grid[0]) or py >= len(grid) or (px, py) in seen:
                continue
            psquare = grid[py][px]
            if psquare == '.':
                continue
            bag.append([px, py, ct + 1])
            seen[(px, py)] = (cx, cy, conv[(dx, dy)])

    if not poss:
        raise Exception
    
    f_paths = []
    for p in poss:
        fx, fy = p
        f_paths.append([get_path(fx, fy, seen)])
    return fx, fy, f_paths
 
def get_sequence(grid, aim):
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == 'A':
                cx, cy = x, y

    sequence = []
    for a in aim:
        cx, cy, n_seq = single(grid, cx, cy, a)
        sequence.extend(n_seq)

    return sequence
def main():
    codes = read_file(get_input_file()).splitlines()

    first_grid = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        ['.', '0', 'A']
    ]

    second_grid = [
        ['.', '^', 'A'],
        ['<', 'v', '>']
    ]

    count = 0
    # it is possible for 2 equal routes to be difference length in the lower layers
    for code in codes: 
        seq = get_sequence(first_grid, code)
        print('seq1', seq)
        o_seq = seq
        seq = []
        for s in o_seq:
            seq.extend(get_sequence(second_grid, s))
            o_seq = seq
            seq = []
            for s in o_seq:
                seq.extend(get_sequence(second_grid, s))
        count += min([len(x) for x in seq]) * int(list(re.findall('\d+', code))[0])
        print(int(list(re.findall('\d+', code))[0]), len(seq))
    return count
if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
