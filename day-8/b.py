from sys import argv
from time import perf_counter
from collections import defaultdict
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


def get_locations(grid, ant):
    valid = set()
    if len(ant) <= 1:
        return set()
    for ps in it.permutations(ant, 2):
        p1, p2 = ps
        y1, x1 = p1
        y2, x2 = p2
        vector = (y2-y1, x2-x1)
        cy, cx = y2, x2
        while not (cy < 0 or cy >= len(grid) or cx < 0 or cx >= len(grid[0])):
            valid.add((cy, cx))
            cy, cx = cy + vector[0], cx + vector[1]

    return valid


def main():
    grid = read_file(get_input_file()).splitlines()
    positions = defaultdict(list)
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square != '.':
                positions[square].append((y, x))

    valid = set()
    for position in positions.values():
        x = get_locations(grid, position)
        valid.update(x)
    
    
    return len(valid)

if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
