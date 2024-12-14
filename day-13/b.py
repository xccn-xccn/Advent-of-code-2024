from sys import argv
from time import perf_counter
import numpy as np
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
    np.set_printoptions(suppress=True)
    machines = [
        list(map(int, list(re.findall("\d+", x))))
        for x in read_file(get_input_file()).split("\n\n")
    ]
    c_machines = machines
    machines = []
    for m in c_machines:
        m[4] += 10000000000000
        m[5] += 10000000000000
        machines.append(m)
    count = 0
    for mach in machines:
        p = single(mach)
        if p is not False and all(n % 1 <= 10**-2 or n % 1 >= (1 - 10**-2) for n in p):
            count += p[0] * 3 + p[1]

    return count


def single(machine):
    b1, b2 = machine[:4:2], machine[1:4:2]
    m1 = [b1, b2]
    m2 = machine[4:]
    if np.linalg.det(m1) == 0:
        return False
    return np.matmul(np.linalg.inv(m1), m2)


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
