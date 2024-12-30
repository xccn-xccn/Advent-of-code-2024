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


def gate_order(l):
    v1 = (
        int(l[0][1:])
        if l[0][1:].isdigit()
        else int(l[3][1:]) if l[3][1:].isdigit() else float("inf")
    )
    v2 = -ord(l[1][0]) if l[0][1:].isdigit() else 1
    return v1, v2


def find_gate(sub, gates, lenient=False, required=None):
    if required == None:
        required = ""
    found = []
    for g in gates:
        if (sub == g[: len(sub)] and not lenient) or (
            lenient and any([x in g[:2] for x in sub]) and required in g
        ):
            found.append(g)

    if len(found) != 1:
        raise Exception(found)
    return found[0]


def single(i, known, gates):  # assumes 2 switched gates are never in the same equation
    switched = []
    n = str(int(gates[i][0][1:]))

    z_i = i
    while "z" + f"{n:0>2}" not in gates[z_i]:
        z_i += 1

    known["r" + n] = gates[i][-1]
    if "XOR" not in gates[z_i]:
        switched.append(gates[z_i][-1])
    else:
        z_gate = gates[z_i][:2]

        p1 = sorted([(known["r" + n], "r" + n),(known["c" + str(int(n) - 1)], "c" + str(int(n) - 1))], reverse=True)
        for val, key in p1:
            if val not in z_gate:
                for z in z_gate:
                    if z not in [x[0] for x in p1]:
                        switched.append(val)
                        known[key] = z
                        break

    known["a" + n] = gates[i + 1][-1]
    known["p" + n] = find_gate(
        sorted([known["r" + n], known["c" + str(int(n) - 1)]], reverse=True) + ["AND"],
        gates,
    )[-1]

    p2 = sorted([(known["a" + n], "a" + n), (known["p" + n], "p" + n)], reverse=True)
    c_gate = find_gate([p[0] for p in p2], gates, lenient=True, required="OR")

    for val, key in p2:
        if val not in c_gate:
            for c in c_gate:
                if c not in [x[0] for x in p2]:
                    switched.append(val if "z" not in val else c)
                    known[key] = c
                    break

    if len(switched) == 1:
        p = find_gate(
            sorted([known["r" + n], known["c" + str(int(n) - 1)]], reverse=True),
            gates,
            lenient=True,
            required="XOR",
        )[-1]
        if "z" not in p:
            switched.append(p)

    known["c" + n] = c_gate[-1]

    return known, switched


def main():
    gates = read_file(get_input_file()).split("\n\n")[1]
    known = {}

    switched = set()
    gates = sorted(
        [re.findall("[a-zA-Z0-9]+", x) for x in gates.splitlines()], key=gate_order
    )

    known["c0"] = gates[1][-1]
    gates = gates[2:]
    gates = [sorted(g[:-1], reverse=True) + [g[-1]] for g in gates]

    i = 0
    for p in range(1, 45):
        while True:
            if gates[i][0][1:].isdigit() and int(gates[i][0][1:]) == p:
                break
            i += 1

        known, new = single(i, known, gates)
        switched.update(new)

    return ",".join(sorted(switched))


if __name__ == "__main__":
    start = perf_counter()
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
