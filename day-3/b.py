from sys import argv
from time import perf_counter
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
    text = "".join(read_file(get_input_file()).split())
    found = list(re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", text))
    count= 0

    apply = True
    for p in found:
        if p == 'do()':
            apply = True
        elif p == "don't()":
            apply = False
        elif apply:
            n1, n2 = re.findall("\d+", p)
            count += int(n1) * int(n2)

    return count
if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')