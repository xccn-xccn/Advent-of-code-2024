from sys import argv
from time import perf_counter

def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def get_score(grid, start):
    seen = set([start])
    bag = [start]
    valid = []
    while bag:
        cy, cx = bag.pop()
        csquare = int(grid[cy][cx])
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if dy == dx == 0:
                continue
            py, px = cy + dy, cx + dx
            if py < 0 or py >= len(grid) or px < 0 or px >= len(grid[0]) or grid[py][px] == '.':
                continue
            psquare = int(grid[py][px])
            if csquare != psquare - 1 or (py, px) in seen:
                continue
            seen.add((py, px))
            if psquare != 9:
                bag.append((py, px))
            else:
                valid.append((py, px))

    return valid


def main():
    grid = read_file(get_input_file()).splitlines()
    starts = []
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == '0':
                starts.append((y, x))

    count = 0
    for start in starts:
        p = get_score(grid, start)
        count += len(p)

    return count


if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')