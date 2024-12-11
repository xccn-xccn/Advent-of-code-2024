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


def main():
    stones = [int(x) for x in read_file(get_input_file()).split()]
    for _ in range(25):
        new = []
        for s in stones:
            str_s = str(s)
            if s == 0:
                new.append(1)
            elif len(str_s) % 2 == 0:
                new.append(int(str_s[: len(str_s) // 2]))
                new.append(int(str_s[len(str_s) // 2 :]))
            else:
                new.append(s * 2024)

        stones = new

    return len(stones)


if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
