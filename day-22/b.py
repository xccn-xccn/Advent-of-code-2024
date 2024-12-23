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


def single(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return n


def main():
    nums = list(map(int, read_file(get_input_file()).splitlines()))
    sequences = defaultdict(lambda: 0)

    for n in nums:
        last, changes, seen = int(str(n)[-1]), [], set()
        for r in range(2000):
            
            n = single(n)
            v = int(str(n)[-1])
            changes.append(v - last)
            last = v

            if len(changes) >= 4 and tuple(changes[-4:]) not in seen:
                seen.add(tuple(changes[-4:]))
                sequences[tuple(changes[-4:])] += v

    return max(sequences.values())


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
