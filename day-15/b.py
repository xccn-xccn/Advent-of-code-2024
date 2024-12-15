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


def single(cx, cy, dx, dy, grid, second=True):
    px, py = cx + dx, cy + dy

    if px < 0 or py < 0 or px >= len(grid[0]) or py >= len(grid):
        return False
    p_square = grid[py][px]
    valid = False
    changes = {}
    if p_square == "#":
        return False
    elif p_square == ".":
        valid = True

    elif p_square in "[]":
        direction = 1 if p_square == "[" else -1
        c1 = single(px, py, dx, dy, grid)
        if c1 == False:
            return False

        if second or dx == 0:
            c2 = single(px + direction, py, dx, dy, grid, second=False)

            if c2 == False:
                return False
            changes.update(c2)

        changes.update(c1)
        valid = True

    if valid:
        changes.update({(px, py): (cx, cy)})
        return changes


def main():
    o_grid, moves = read_file(get_input_file()).split("\n\n")
    o_grid = list(map(list, o_grid.splitlines()))
    moves = "".join(moves.split())
    convert = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

    grid = []
    for y, row in enumerate(o_grid):
        grid.append([])
        for x, square in enumerate(row):
            if square == "O":
                grid[-1].extend("[]")
            elif square == "@":
                grid[-1].extend("@.")
                cx, cy = x * 2, y
            else:
                grid[-1].extend(square * 2)

    for move in moves:
        dx, dy = convert[move]
        changes = single(cx, cy, dx, dy, grid)

        if changes != False:
            o_grid = grid
            grid = []
            cx, cy = cx + dx, cy + dy

            for y, row in enumerate(o_grid):
                grid.append([])
                for x, square in enumerate(row):
                    if (x, y) in changes.keys():
                        nx, ny = changes[(x, y)]
                        grid[-1].append(o_grid[ny][nx])
                    elif (x, y) in changes.values():
                        grid[-1].append(".")
                    else:
                        grid[-1].append(square)

    count = 0
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == "[":
                count += y * 100 + x

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
