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


def main():
    rules, update = read_file(get_input_file()).split('\n\n')
    rules = [row.split('|') for row in rules.splitlines()]
    f_rules = defaultdict(set)
    for s, e in rules:
        f_rules[s].add(e)
        
    count = 0
    for line in update.splitlines():
        seen = set()
        valid = True
        line = line.split(',')
        for char in line:
            if f_rules.get(char, set()) & seen:
                valid = False
                break
            else:
                seen.add(char)

        if valid:
            count += int(line[len(line)//2])

    return count

if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')