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


def main():
    grid = read_file(get_input_file()).splitlines()
    count = 0
    seen = set()
    while True:
        extra, seen = single_region(grid, seen)
        if extra is False:
            return count
        count += extra


def single_region(grid, seen):
    flag = True
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if (y, x) not in seen:
                pos, plant = (y, x), square
                flag = False
                break
        if not flag:
            break

    if flag:
        return False, False

    seen.add(pos)
    bag = [pos]
    region = [pos]
    sides = 0
    while bag:
        cy, cx = bag.pop()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            py, px = cy + dy, cx + dx
            if (
                py < 0
                or px < 0
                or py >= len(grid)
                or px >= len(grid[0])
                or grid[py][px] != plant
            ):
                continue
            if (py, px) in seen:
                continue
            bag.append((py, px))
            region.append((py, px))
            seen.add((py, px))

    

    r_list = list(zip(*grid[::-1]))
                
            
def get_sides(grid, seen):
    for y1, y2 in zip(range(-1, len(grid)), range(len(grid) + 1)):
        for x1, x2 in zip(range(-1, len(grid[0]), range(len(grid[0])))):
            s1, s2 = (y1, x1) in seen, (y2, x2) in seen
            if s1 ^ s2:
                if i < 0 or (row1[i], row2[i]) != (s1, s2):
                    sides += 1
if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds