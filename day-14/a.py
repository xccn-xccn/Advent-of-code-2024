from sys import argv
from time import perf_counter
from itertools import chain
from functools import reduce
import re


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def single(r, width, height):
    cx, cy = r[:2]
    cx, cy = (cx + r[2] * 100) % width, (cy + r[3] * 100) % height
    return cx, cy


def main():
    robots = [
        list(map(int, list(re.findall("[\-\d]+", x))))
        for x in read_file(get_input_file()).splitlines()
    ]
    width, height = 101, 103
    w_mid, h_mid = (width + 1) / 2 - 1, (height + 1) / 2 - 1
    quadrants = [[0, 0], [0, 0]]
    for r in robots:
        i1 = i2 = None
        nx, ny = single(r, width, height)

        i1 = 0 if nx < w_mid else 1 if nx > w_mid else None
        i2 = 0 if ny < h_mid else 1 if ny > h_mid else None
        if i1 == None or i2 == None:
            continue
        quadrants[i1][i2] += 1

    return reduce(lambda x, y: x * y, (chain.from_iterable(quadrants)))


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
