from sys import argv
from time import perf_counter
from collections import deque, defaultdict
from itertools import groupby
from functools import cache
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


def valid_order(seq):
    order = {"<": "^v", "^": ">", ">": ".", "v": ">"}

    s = [k for k, v in groupby(seq)]
    if len(s) == 2:
        c1, c2 = s

        if c2 not in order[c1]:
            return False

    if len(s) > 2:
        print(seq, s)
        raise Exception

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

        best = min([len(list(groupby(v))) for v in valid])
        valid = [v for v in valid if len(list(groupby(v))) == best]

        if len(valid) > 1:
            valid = [v for v in valid if valid_order(v[::-1])]

    return valid[0][::-1] + ["A"] if valid else ["A"]


@cache
def single(grid, cx, cy, aim):
    sx, sy = cx, cy
    bag = deque([[cx, cy, 0]])
    seen = defaultdict(list)
    conv = {(1, 0): ">", (0, 1): "v", (-1, 0): "<", (0, -1): "^"}
    best = float("inf")

    while bag:

        cx, cy, ct = bag.popleft()
        if grid[cy][cx] == aim:
            fx, fy = cx, cy
            if ct < best:
                best = ct
        if ct > best:
            break

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            px, py = cx + dx, cy + dy

            if (
                px < 0
                or py < 0
                or px >= len(grid[0])
                or py >= len(grid)
                or (cx, cy) in [x[:2] for x in seen[px, py]]
            ):
                continue
            psquare = grid[py][px]
            if psquare == ".":
                continue

            if seen[(px, py)] == []:
                bag.append([px, py, ct + 1])
            seen[(px, py)].append((cx, cy, conv[(dx, dy)]))

    return fx, fy, get_paths(fx, fy, seen, sx, sy)


@cache
def get_sequence(aim, layer, extra=0, start=None):
    if layer == 13 + extra:
        return aim
    if layer == 0:
        cx, cy = 2, 3
        grid = grids[0]
    else:
        cx, cy = 2, 0
        grid = grids[1]

    if start:
        for y, row in enumerate(grid):
            for x, square in enumerate(row):
                if square == start:
                    cx, cy = x, y
                    break

    sequence = []
    for a in aim:
        cx, cy, n_seq = single(grid, cx, cy, a)
        s_seq = get_sequence("".join(n_seq), layer + 1, extra)
        sequence += s_seq

    return sequence


def main():
    global grids

    codes = read_file(get_input_file()).splitlines()

    first_grid = (("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), (".", "0", "A"))
    second_grid = ((".", "^", "A"), ("<", "v", ">"))

    grids = (first_grid, second_grid)

    count = 0
    for code in codes:

        sequence = get_sequence(code, 0, extra=0)
        s_count = len(get_sequence(sequence[0], 1, extra=1))

        for s1, s2 in zip(sequence, sequence[1:]):
            s_count += len(get_sequence(s2, 1, extra=1, start=s1))

        count += s_count * int(list(re.findall("\d+", code))[0])

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
