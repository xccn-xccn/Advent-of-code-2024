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


def binary_search(bag, aim):
    l, h = 0, len(bag) - 1
    m = 0
    while l <= h:
        m = (l + h) // 2

        p = bag[m][3]
        if p == aim:
            return m
        elif p < aim:
            h = m - 1
        else:
            l = m + 1

    return m


def main():
    grid = list(map(list, read_file(get_input_file()).splitlines()))
    for row in grid:
        print(row)
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == 'S':
                pos = (x, y, 0, 0)
                print('found')
                break

    conv = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    seen = {pos: 0}
    bag = [pos]
    valid = None
    while bag:
        print(bag)
        cx, cy, cd, cs = bag.pop()
        for p in (1, -1, 0):
            pd = (cd + p) % 4
            dx, dy = conv[pd]
            px, py, ps = cx + dx, cy + dy, cs + 1 + 1000 * abs(p)
            if px < 0 or px >= len(grid[0]) or py < 0 or py >= len(grid) or grid[px][py] =='#' or seen.get((px, py, pd), float('inf')) < ps:
                continue
            if grid[px][py] == 'E':
                print('end')
                if valid and ps >= valid:
                    return valid
                else:
                    valid = ps
            else:
                bag.insert(binary_search(bag, ps), (px, py, pd, ps))
                seen[(px, py, pd)] = ps
        
        

if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f'Time taken: {(perf_counter() - start) *1000} miliseconds')