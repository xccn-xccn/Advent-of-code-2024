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
    text = list(map(int, list(read_file(get_input_file())))
    print(len(text))
    front = (0, 1)
    back  = (0, text[-1])
    text_i = 0
    real_i = 0
    check_sum = 0
    while (front[0] + back[0], front[1] + back[1]) != (len(text) - 1, text[-1]):
        if pos % 2:
            checksum += real_i * front[0]
            if front[1] == text[text_i]:
                front[0] += 1
                text_i += 1
            else:
                front[1] += 1
        else:
            checksum += real_i * ((len(text) // 2 + 1) - back[0])
            if back[1] == 0:
                back[0] += 1
                text_i += 1
            else:
                back[1] -= 1

        real_i += 1
if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')