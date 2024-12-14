from sys import argv
from time import perf_counter
from collections import defaultdict
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


def main():
    machines = [
        list(map(int, list(re.findall("\d+", x))))
        for x in read_file(get_input_file()).split("\n\n")
    ]
    possible = []
    for mach in machines:
        p = single(mach)
        if p != float("inf"):
            possible.append(p)

    return sum(possible)


def single(machine):
    bag = [(0, (0, 0))]  # tokens score
    best = float("inf")
    seen = defaultdict(lambda: float("inf"))
    while bag:
        ct, cp = bag.pop()
        cx, cy = cp
        for dt, d in zip((3, 1), (machine[:2], machine[2:4])):
            dx, dy = d
            pt, px, py = ct + dt, cx + dx, cy + dy
            if px > machine[4] or py > machine[5] or seen[(px, py)] <= pt:
                continue
            if px == machine[4] and py == machine[5]:
                if pt < best:
                    best = pt
                else:
                    return pt
            else:
                bag.insert(binary_search(bag, pt), (pt, (px, py)))
                seen[(px, py)] = pt

    return best


def binary_search(bag, aim):
    l, h = 0, len(bag) - 1
    m = 0
    while l <= h:
        m = (l + h) // 2

        p = bag[m][0]
        if p == aim:
            return m
        elif p < aim:
            h = m - 1
        else:
            l = m + 1

    return m


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
