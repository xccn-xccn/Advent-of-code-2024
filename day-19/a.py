import re
from sys import argv
from time import perf_counter
from collections import defaultdict


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def valid(design, patterns):
    bag = [""]
    while bag:

        c = bag.pop()
        for p in patterns[design[len(c)]]:
            if design[len(c) : len(c) + len(p)] != p:
                continue
            if c + p == design:
                return True
            bag.append(c + p)

    return False


def main():
    t_patterns, designs = read_file(get_input_file()).split("\n\n")
    patterns = defaultdict(list)
    for p in re.findall("[a-z]+", t_patterns):
        patterns[p[0]].append(p)
    designs = designs.splitlines()

    count = 0
    for d in designs:
        if valid(d, patterns):
            count += 1

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
