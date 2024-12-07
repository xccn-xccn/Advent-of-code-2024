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


def valid(line):
    aim = line[0]
    current = [line[1]]
    for n in line[2:]:
        current_copy = current.copy()
        current = []
        while current_copy:
            c = current_copy.pop()
            current.append(c * n)
            current.append(c + n)

    return aim in current

def main():
    numbers = [list(map(int, list(re.findall('\d+', line)))) for line in read_file(get_input_file()).splitlines()]
    count = 0
    for row in numbers:
        if valid(row):
            count += row[0]
    return count
            

if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
