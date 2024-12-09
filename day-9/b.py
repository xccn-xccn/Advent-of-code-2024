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


def main():
    text = list(map(int, list(read_file(get_input_file()))))
    disk = []
    nums = defaultdict(lambda : [(-1, -1)])
    for i, n in enumerate(text):
        if i % 2 == 0:
            for n1 in range(n, 10):
                nums[n1].append((i, n))

    seen = set()
    for i, n in enumerate(text):
        if i % 2 == 0 and i not in seen:
            seen.add(i)
            disk.extend([i // 2] * n)
        else:
            space = n 
            while space:

                for p in reversed(nums[space]):
                    if p[0] not in seen or i > p[0]:
                        break
                if i < p[0]:
                    disk.extend([p[0] // 2] * p[1])
                    seen.add(p[0])
                    space -= p[1]
                else:
                    break

            disk.extend([0] * space)

    check_sum = 0
    for i, d in enumerate(disk):
        check_sum += d * i
    return check_sum


if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
