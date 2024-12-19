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

def get_pos(a):
    n = 1
    while True:
        if a < 8 ** n:
            return n
        n += 1

def valid_start(a, aim):
    reg = [a]
    reg.append((a % 8) ^ 2)
    reg.append(reg[0] // 2**reg[1])
    reg[1] = reg[1] ^ reg[2] ^ 3
    if reg[1] % 8 != int(aim[-get_pos(a)]):
        return False
    
    return True

def single_repetition(f_a, aim):
    poss = []
    for n in range(f_a * 8 + 7, f_a * 8 - 1, -1):
        if valid_start(n, aim):
            if n >= 8**15:
                return n
            poss.append(n)
    return poss


def main():
    text = list(map(int, re.findall('\d+', read_file(get_input_file()))))
    aim = text[3:]
    bag = [0]
    
    while bag:
        c = bag.pop()
        p = single_repetition(c, aim)
        if isinstance(p, list):
            bag.extend(p)
        else:
            return p 

if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')