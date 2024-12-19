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


def get_operand(n, reg):
    if n == 7:
        raise Exception(n, reg)
    if n <= 3:
        return n
    return reg[n-4]
    
def single(instructions, pointer, reg, output):

    if pointer >= len(instructions):
        return [str(x) for x in output]
    
    opcode, l_operand = instructions[pointer: pointer + 2]
    inc = True
    if opcode == 0:
        reg[0] = reg[0] // (2 ** get_operand(l_operand, reg)) 
    elif opcode == 1:
        reg[1] = reg[1] ^ l_operand
    elif opcode == 2:
        reg[1] = get_operand(l_operand, reg) % 8
    elif opcode == 3:
        if reg[0]:
            pointer = l_operand
            inc = False
    elif opcode == 4:
        reg[1] = reg[1] ^ reg[2]
    elif opcode == 5:
        output.append(get_operand(l_operand, reg) % 8)
    else:
        reg[opcode-5] = reg[0] // (2 ** get_operand(l_operand, reg)) 

    if inc:
        pointer += 2
    
    return single(instructions, pointer, reg, output)



def main():
    text = list(map(int, re.findall('\d+', read_file(get_input_file()))))
    reg, instructions = text[:3], text[3:]

    return ",".join(single(instructions, 0, reg, []))
    
if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')