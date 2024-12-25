from sys import argv
from time import perf_counter


def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"


def valid(lock, key):
    for l, k in zip(lock, key):
        if l + k > 5:
            return False

    return True


def main():
    items = [
        list(map(list, x.splitlines()))
        for x in read_file(get_input_file()).split("\n\n")
    ]
    counts = [[], []]
    for item in items:
        if item[0][0] == "#":
            i = 0
        else:
            i = 1
        single = []
        for x in range(len(item[0])):
            single.append([row[x] for row in item[1:-1]].count("#"))

        counts[i].append(single)

    count = 0
    for lock in counts[0]:
        for key in counts[1]:
            if valid(lock, key):
                count += 1

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
