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
    text = [int(n) for x in read_file(get_input_file()).splitlines() for n in x.split()]
    l1, l2 = text[::2], text[1::2]

    return sum([abs(n1- n2) for n1, n2 in zip(l1, l2)])


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
