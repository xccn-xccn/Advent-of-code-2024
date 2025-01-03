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


def main():
    grid = read_file(get_input_file()).splitlines()
    pos = list(((y, x) for y, row in enumerate(grid) for x, square in enumerate(row) if square == '^'))

    cy, cx = pos[0]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    di = 0
    seen = set([(cy, cx)])
    while True:
        dy, dx = directions[di]
        py, px = cy + dy, cx + dx
        
        if py < 0 or py >= len(grid) or px < 0 or px >= len(grid[0]):
            break
        if grid[py][px] == '#':
            di = (di + 1) % 4
        else:
            cy, cx = py, px
            seen.add((py, px))
        
    return len(seen)
        

if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')