from sys import argv
from time import perf_counter
from collections import deque


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def main():
    grid = read_file(get_input_file()).splitlines()
    starts = [
        (y, x)
        for y, row in enumerate(grid)
        for x, square in enumerate(row)
        if square == "X"
    ]
    count = 0

    for start in starts:
        cy, cx = start
        for dy, dx in (
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ):

            for i in range(1, 4):

                py, px = cy + dy * i, cx + dx * i
                if py < 0 or py + 1 > len(grid) or px < 0 or px + 1 > len(grid[0]):
                    continue

                if grid[py][px] == "XMAS"[i]:
                    if i == 3:
                        count += 1
                else:
                    break

    return count


if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
