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


def calc(n1, n2, op):
    if op == 'AND':
        return n1 and n2
    elif op == "OR":
        return n1 or n2
    else:
        return n1 ^ n2
    
def main():
    wires, gates = read_file(get_input_file()).split('\n\n')
    # known = [(k, v) for line in wires.splitlines() for k, v in (line.split(':'))]
    known = {line.split(':')[0]: int(line.split(':')[1]) for line in wires.splitlines()}
    print(known)

    # print(known)
    gates = [re.findall('[a-zA-Z0-9]+', x) for x in gates.splitlines()]
    cont = True
    while cont:
        cont = False
        for gate in gates:
            w1, op, w2, w3 = gate
            if w1 not in known or w2 not in known or w3 in known:
                continue

            known[w3] = calc(known[w1], known[w2], op)
            cont = True

    valid = [(k, v) for k, v in known.items() if k[0] == 'z']
    valid = sorted(valid, key=lambda x: x[0], reverse=True)
    print(valid)
    return int(''.join(str(x[1]) for x in valid), 2)

    # print(gates)


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
