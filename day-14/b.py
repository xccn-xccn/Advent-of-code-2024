from sys import argv
from time import perf_counter
from itertools import product
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


def single(t, r, width, height):
    cx, cy = r[:2]
    cx, cy = (cx + r[2] * t) % width, (cy + r[3] * t) % height
    return cx, cy


def display(valid, width, height, t, count):
    output = ""
    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) in valid:
                line += "\u25A0"
            else:
                line += "\u25A1"

        output += line + "\n"

    print(output, t, count, "\n\n\n")


def next_count(valid, nx, ny):
    count = 0
    for dx, dy in product([0, 1, -1], repeat=2):
        if dy == dx == 0:
            continue
        if (nx + dx, ny + dy) in valid:
            count += 1

    return count


def main():  # t = 6587
    robots = [
        list(map(int, list(re.findall("[\-\d]+", x))))
        for x in read_file(get_input_file()).splitlines()
    ]
    print(len(robots))
    if len(argv) == 2:
        width, height = 101, 103
    else:
        width, height = 11, 7

    best = 0
    t = 0
    while True:
        count = 0
        valid = set()
        for r in robots:
            nx, ny = single(t, r, width, height)
            valid.add((nx, ny))
            count += next_count(valid, nx, ny)

        if count >= best:
            best = count
            display(valid, width, height, t, count)

        t += 1


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
