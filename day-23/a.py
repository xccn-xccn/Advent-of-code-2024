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


def get_parties(connections, v, current):
    if not current:
        return []
    if len(current[0]) == 3:
        return [tuple(sorted(x)) for x in current]
    parties = []
    for c in current:
        for d in v:
            if d not in c and all(d in connections[x] for x in c):
                parties.append(c + [d])

    return get_parties(connections, v, parties)

def main():
    links = [x.split('-') for x in read_file(get_input_file()).splitlines()]
    connects = defaultdict(set)
    for l in links:
        for c in l:
            connects[c].update(l)

    poss = set()
    for v in connects.values():
        p = get_parties(connects, v, links)
        if p:
            poss.update(p)


    valid = []
    for x in poss:
        if any(c[0] == 't' for c in x):
            valid.append(x) 

    return len([x for x in poss if any(c[0] == 't' for c in x)])


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
