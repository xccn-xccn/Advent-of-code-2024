from sys import argv
from time import perf_counter
import re
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


def turn(n):
    return -1 if n < 0 else 1
def main():
    cubes = [[x[:2]] + [int(y) for y in re.findall('-?\d+', x)] for x in read_file(get_input_file()).splitlines()]
    print(cubes)

    on = set()
    for cube in cubes:
        if any(abs(x) > 50 for x in cube[1:]):
            continue
        t, x1, x2, y1, y2, z1, z2 = cube
        xs, ys, zs = turn(x2 - x1 + 1), turn(y2 - y1 + 1), turn(z2 - z1 + 1)
        cs = list(it.product(range(x1, x2 + xs, xs), range(y1, y2 + ys, ys), range(z1, z2 + zs, zs)))
        # print(list(range(x1, x2 + xs, xs)))
        if t == 'on':
            on.update(cs)
        else:
            on.difference_update(cs)

    return len(on)

if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
