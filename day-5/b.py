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

def single(line, rules):
    seen = set()
    for char in line:
        if rules.get(char, set()) & seen:
            return new_list(line, char, rules.get(char, set()) & seen)
        else:
            seen.add(char)

    return line

def new_list(line, aim, to_move):
    new = []
    move_c = list(to_move)
    for char in line:
        if char in to_move:
            continue
        elif char == aim:
            new.append(char)
            new += move_c
        else:
            new.append(char)

    return new
        


def main():
    rules, update = read_file(get_input_file()).split('\n\n')
    update = [line.split(',') for line in update.splitlines()]
    rules = [row.split('|') for row in rules.splitlines()]
    f_rules = defaultdict(set)
    for s, e in rules:
        f_rules[s].add(e)
        
    count = 0
    for line in update:

        l = single(line, f_rules)
        if l == line:
            continue
        old = []
        while old != l:
            old = l
            l = single(l, f_rules)
        
        count += int(l[len(l) // 2])

    return count

if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')