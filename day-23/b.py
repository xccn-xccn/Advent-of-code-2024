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


def get_parties(connections, v, current, seen):
    seen = set()
    best = []
    while current:
        c = current.pop()
        if len(c) > len(best):
            best = c
        for d in v:
            if d in c:
                continue
            p = sorted(c + [d])
            if tuple(p) not in seen and all(d in connections[x] for x in c):
                current.append(p)
                seen.add(tuple(p))
            
    return best, seen

def main():
    links = [x.split('-') for x in read_file(get_input_file()).splitlines()]
    connects = defaultdict(set)
    for l in links:
        for c in l:
            connects[c].update(l)

    best = []
    seen = set()
    for v in connects.values():
        p, seen = get_parties(connects, list(v), [[]], seen)
        if len(p) > len(best):
            best = p

    return ','.join(sorted(best))


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')
