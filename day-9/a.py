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
    text = list(map(int, list(read_file(get_input_file()))))
    print(text)
    print(len(text))
    disk = []
    pos = [0, 1]
    back = [len(text) - 1, 1]
    while pos[0] < len(text):
        n = text[pos[0]]
        if (pos[0] + 1) % 2:
            disk.append(pos[0] // 2)
        else:
            disk.append(back[0] // 2)
            if back[1] == text[back[0]]:
                back[0] -= 2
                back[1] = 1
            else:
                back[1] += 1

        if pos[1] == n:
            pos[0] += 1
            pos[1] = 1
        else:
            pos[1] += 1

        # print(pos, back)
        if pos[0] > back[0] or (pos[0] == back[0] and pos[1] > (text[pos[0]] - back[1] + 1)):
            break

    check_sum = 0
    print(disk)
    for i, d in enumerate(disk):
        check_sum += d * i



    return check_sum 
if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')