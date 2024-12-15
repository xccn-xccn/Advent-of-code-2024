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


def single(cx, cy, dx, dy, grid):
    px, py = cx + dx, cy + dy

    if px < 0 or py < 0 or px >= len(grid[0]) or py >= len(grid):
        return False
    square = grid[cy][cx]
    p_square = grid[py][px]
    if p_square == "#":
        return False
    elif p_square == ".":
        grid[py][px] = square
        grid[cy][cx] = "."
        return grid
    else:
        grid = single(px, py, dx, dy, grid)
        if grid == False:
            return False
        grid[py][px] = square
        grid[cy][cx] = "."
        return grid


def main():
    grid, moves = read_file(get_input_file()).split("\n\n")
    grid = list(map(list, grid.splitlines()))
    moves = "".join(moves.split())
    convert = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == "@":
                cx, cy = x, y
                break

    for move in moves:
        dx, dy = convert[move]
        p_grid = single(cx, cy, dx, dy, grid)
        if p_grid != False:
            grid = p_grid
            cx, cy = cx + dx, cy + dy

    count = 0
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == "O":
                count += y * 100 + x

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
