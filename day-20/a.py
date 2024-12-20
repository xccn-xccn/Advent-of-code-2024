from sys import argv
from time import perf_counter
import itertools as it


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def get_route(grid):
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == 'S':
                cx, cy = x, y
                break

    t = 0
    times = {(cx, cy): 0}
    while grid[cy][cx] != 'E':
        t += 1
        # print(cx, cy)
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            px, py = cx + dx, cy + dy
            if px < 0 or py < 0 or px >= len(grid[0]) or py >= len(grid) or (px, py) in times or grid[py][px] == '#':
                continue
            cx, cy = px, py
            times[(cx, cy)] = t
            break
    
    return times


def main():
    grid = list(map(list, read_file(get_input_file()).splitlines()))
    times = get_route(grid)
    count = 0
    for pos, ct in times.items():
        cx, cy = pos
        for dx, dy in ((2, 0), (0, 2), (-2, 0), (0, -2)):
            px, py = cx + dx, cy + dy
            if times.get((px, py), -1) - ct - 2 >= 100:
                count += 1

    return count




if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
