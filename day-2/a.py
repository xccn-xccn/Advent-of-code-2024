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
    text = [
        [int(x) for x in line.split()]
        for line in read_file(get_input_file()).splitlines()
    ]
    count = 0

    for line in text:
        direction = None
        valid = True
        for n1, n2 in zip(line, line[1:]):
            if direction == None:
                if n1 == n2 or abs(n1 - n2) > 3 or abs(n1 - n2) < 1:
                    valid = False
                if n1 < n2:
                    direction = "up"
                elif n1 > n2:
                    direction = "down"

            elif direction == "up":
                if not (1 <= (n2 - n1) <= 3):
                    valid = False

            elif direction == "down":
                if not (1 <= (n1 - n2) <= 3):
                    valid = False

            if valid == False:
                break
        if valid:
            count += 1

    return count


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
