from sys import argv
from time import perf_counter
import math
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


def get_oprand(n, reg):
    if n == 7:
        raise Exception(n, reg)
    if n <= 3:
        return n
    return reg[n-4]
    
def single(instructions, pointer, reg):
    opcode, c_operand = instructions[pointer: pointer + 2]
    if opcode == 0:
        reg[0] = reg[0] / (2 ** c_operand) 
    if opcode == 1:
        reg[1] = reg[1] ^ get_oprand(c_operand)

def main():
    text = list(map(int(re.findall('\d+', read_file(get_input_file())))))
    reg, instructions = text[:3], text[3:]

    while True:
        pass
    
    
    opcode = {}

if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')