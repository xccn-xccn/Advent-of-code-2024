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


def valid(invalid, dimensions):
    invalid = invalid.copy()
    bag = deque([(0, 0)])

    while bag:
        cx, cy = bag.pop()

        for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            px, py = cx + dx, cy + dy
            if (
                px < 0
                or px >= dimensions
                or py < 0
                or py >= dimensions
                or (px, py) in invalid
            ):
                continue
            if px == py == dimensions - 1:
                return True
            bag.append((px, py))
            invalid.add((px, py))
    return False

def main():
    if len(argv) == 2:
        dimensions = 71
        memory = 1024
    else:
        dimensions = 7
        memory = 12

    bites = [tuple(map(int, x.split(",")))
    for x in read_file(get_input_file()).splitlines()]
    
    invalid = {x for x in bites[:memory]}
    invalid.add((0, 0))

    while True:
        memory += 1
        invalid.add(bites[memory])
        if not valid(invalid, dimensions):
            return ','.join([str(x) for x in bites[memory]])
    


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
