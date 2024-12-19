import re
from sys import argv
from time import perf_counter
from collections import defaultdict, deque


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def single(design, patterns):
    t_patterns = patterns
    patterns = defaultdict(list)
    for p in t_patterns:
        if p in design:
            patterns[p[0]].append(p)

    bag = deque([["", 1]])
    count = 0
    while bag:
        c, cw = bag.popleft()

        for d in patterns[design[len(c)]]:
            p = c + d
            if design[len(c) : len(c) + len(d)] != d:
                continue
            if p == design:
                count += cw
                continue
            for i, x in enumerate(bag):
                if x[0] == p:
                    bag[i][1] += cw
                    break
            else:
                bag.append([p, cw])

    return count


def main():
    t_patterns, designs = read_file(get_input_file()).split("\n\n")
    patterns = re.findall("[a-z]+", t_patterns)
    designs = designs.splitlines()

    count = 0
    for d in designs:
        count += single(d, patterns)

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
