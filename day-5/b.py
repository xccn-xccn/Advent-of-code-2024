from sys import argv
from time import perf_counter
from collections import defaultdict 

def read_file(filename):
    with open(filename) as file:
        text = file.read()
    return text


def get_input_file():
    if len(argv) == 1:
        return "sample.txt"
    elif len(argv) == 2:
        return argv[1] if argv[1] != "i" else "input.txt"

def valid(line, rules):
    seen = set()
    for i, char in enumerate(line):
        if f_rules.get(char, set()) & seen:
            return i
        else:
            seen.add(char)

    return True

def new_list(line, aim, to_move):
    new = []
    move_c = []
    for char in line:
        if char in to_move:
            move_c.append(char)
        elif char == aim:
            new += move_c
            new.append(char)
        else:
            new.append(char)
        


def main():
    rules, update = read_file(get_input_file()).split('\n\n')
    update = [line.split(',') for line in update.splitlines()]
    rules = [row.split('|') for row in rules.splitlines()]
    f_rules = defaultdict(set)
    for s, e in rules:
        f_rules[s].add(e)
        
    print(f_rules)
    count = 0
    for line in update:
        print(line)

        if valid:
            count += int(line[len(line)//2])

    return count

if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')