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
    if len(argv) == 2:
        dimensions = 71
        memory = 1024
    else:
        dimensions = 7
        memory = 12
    invalid = {
        tuple(map(int, x.split(",")))
        for x in read_file(get_input_file()).splitlines()[:memory]
    }
    invalid.add((0, 0))
    bag = deque([(0, 0)])
    count = 0

    while bag:
        count += 1
        for r in range(len(bag)):
            cx, cy = bag.popleft()

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
                    return count
                bag.append((px, py))
                invalid.add((px, py))


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
