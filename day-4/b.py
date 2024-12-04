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
        if square == "A"
    ]
    count = 0

    for start in starts:
        cy, cx = start
        letters = []
        for dy, dx in ((1, -1), (-1, 1), (1, 1), (-1, -1)):
            py, px = cy + dy, cx + dx
            if py < 0 or py + 1 > len(grid) or px < 0 or px + 1 > len(grid[0]):
                break
            letters.append(grid[py][px])

        if sorted(letters[:2]) == sorted(letters[2:]) == ["M", "S"]:
            count += 1
    return count


if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
