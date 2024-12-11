from sys import argv
from time import perf_counter
from functools import cache


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
    stones = [int(x) for x in read_file(get_input_file()).split()]
    count = 0
    for s in stones:
        count += get_stones(s, 75)

    return count


@cache
def get_stones(stone, rem):
    if rem == 0:
        return 1

    str_s = str(stone)
    if stone == 0:
        return get_stones(1, rem - 1)
    elif len(str_s) % 2 == 0:
        return get_stones(int(str_s[: len(str_s) // 2]), rem - 1) + get_stones(
            int(str_s[len(str_s) // 2:]), rem - 1)
    else:
        return get_stones(stone * 2024, rem - 1)


if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
