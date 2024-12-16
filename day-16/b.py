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
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if square == "S":
                pos = (x, y, 0, 0, set([(0, 0)]))
                break

    conv = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    seen = {pos[:-1]: 0}
    bag = [pos]
    valid = []
    while bag:
        cx, cy, cd, cs, cpath = bag.pop()
        for p in (1, -1, 0, 2):
            pd = (cd + p) % 4
            dx, dy = conv[pd]
            px, py, ps = cx + dx, cy + dy, cs + 1 + 1000 * abs(p)
            if (
                px < 0
                or px >= len(grid[0])
                or py < 0
                or py >= len(grid)
                or grid[py][px] == "#"
                or seen.get((px, py, pd), float("inf")) < ps
            ):
                continue

            p_path = cpath.copy()
            p_path.add((px, py))
            if grid[py][px] == "E":
                if valid and ps > valid[0][0]:
                    break
                else:
                    valid.append((ps, p_path))
            else:
                bag.insert(binary_search(bag, ps), (px, py, pd, ps, p_path))
                seen[(px, py, pd)] = ps

    final = set()
    for v in valid:
        final.update(v[1])

    return len(final)


if __name__ == "__main__":
    start = perf_counter()

    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
