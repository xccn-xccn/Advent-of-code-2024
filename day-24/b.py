from sys import argv
from time import perf_counter
from collections import defaultdict
import re

#TODO case where yn . xn -> zn breaks everything to fix make it search instead of adding 1/2 to the index
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
    if op == "AND":
        return n1 and n2
    elif op == "OR":
        return n1 or n2
    else:
        return n1 ^ n2


def gate_order(l):
    v1 = (
        int(l[0][1:])
        if l[0][1:].isdigit()
        else int(l[3][1:]) if l[3][1:].isdigit() else float("inf")
    )
    v2 = -ord(l[1][0]) if l[0][1:].isdigit() else 1
    return v1, v2


def difference(l1, l2):
    for i, v1, v2 in zip(range(len(l1)), l1, l2):
        if v1[0] != v2:
            return i, v1

    raise Exception(l1, l2)


def find_gate(sub, gates, lenient=False, required=None):
    if required == None:
        required = ''
    found = []
    for g in gates:
        # if g[0] == 'wrn':
        #     print(g[:], sub)
        # if lenient:
        #     print
        # print((lenient and any([x in g[:2] for x in sub]) and required in g))
        if (sub == g[: len(sub)] and not lenient) or (lenient and any([x in g[:2] for x in sub]) and required in g):
            print(required, g, required in g, lenient)
            found.append(g)
            print(found)

    if len(found) != 1:
        raise Exception(found)
    return found[0]


def single(i, known, gates):  # assumes 2 switched gates are never in the same equation
    #BUG assumes zn is never in the wrong place
    

    z_gate = None

    # i = p * 3
    n = str(int(gates[i][0][1:]))

    z_i = i
    while 'z' + f'{n:0>2}' not in gates[z_i]:
        z_i += 1


    print(n, gates[i:i+3], i, z_i, gates[z_i])
    switched = []

    known["r" + n] = gates[i][-1]
    

    if "XOR" not in gates[z_i]: #if z is swapped with z it will not work
        print('XOR not in')
        switched.append(gates[z_i][-1])
        print(known)
        #not actually neccessary because there are not 2 switched gates in 1 equation
        if known["c" + str(int(n) - 1)] not in find_gate([known['r' + n], ''], gates, lenient=True, required='XOR'):
            switched.append(known["c" + str(int(n) - 1)])
            print(known)
            print(known["c" + str(int(n) - 1)])
            raise Exception
        elif known['r' + n] not in find_gate([known["c" + str(int(n) - 1)], ''], gates, lenient=True, required='XOR'):
            print(known)
            raise Exception
    else:
        z_gate = gates[z_i][:2]
        # if [p[0] for p in p1] != z_gate:
        #     d_i, diff = difference(p1, z_gate)
        #     switched.append(diff)
        #     known[p1[d_i][1]] = z_gate[d_i]

        p1 = sorted(
        [
            (known["r" + n], "r" + n),
            (known["c" + str(int(n) - 1)], "c" + str(int(n) - 1)),
        ], reverse=True
        )
        print('p1', p1, z_gate)
        for p in p1:
            val, key = p
            if val not in z_gate:
                for z in z_gate:
                    if z not in [x[0] for x in p1]:
                        switched.append(val)
                        known[key] = z
                        break
                # switched.append(val)
                # known[key] = z

    known["a" + n] = gates[i + 1][-1]
    print('z_gate', z_gate, sorted([known['r' + n], known['c' + str(int(n) - 1)]], reverse=True))
    known["p" + n] = find_gate(sorted([known['r' + n], known['c' + str(int(n) - 1)]], reverse=True) + ['AND'], gates)[-1]

    p2 = [(known["a" + n], "a" + n), (known["p" + n], "p" + n)]
    c_gate = find_gate([p[0] for p in p2], gates, lenient=True, required='OR')
    print('p2', p2, c_gate)
    for p in p2: #does not work if z is swapped with c because if z is swapped it assumes 
        val, key = p
        if val not in c_gate:
            for c in c_gate:
                if c not in [x[0] for x in p2]:
                    print(known)
                    switched.append(val if 'z' not in val else c)
                    # if val != 'ndw':
                    #     raise Exception(val)
                    known[key] = c
                    break
        
    if len(switched) == 1:
        p = find_gate(sorted([known['r' + n], known['c' + str(int(n) - 1)]], reverse=True), gates, lenient=True, required='XOR')[-1]
        if 'z' not in p:
            switched.append(p)

    known["c" + n] = c_gate[-1]

    print("known", known)
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
    for g in gates:
        print(g)

    i = 0
    for p in range(1, 45):
        while True:
            if gates[i][0][1:].isdigit() and int(gates[i][0][1:]) == p:
                break
            i += 1

        print(p, i, gates[i])
        known, new = single(i, known, gates)
        if new:
            print('new', new)
        switched.update(new)

        # print('switched', sorted(switched))
    print(switched)
    # switched.add('ggn')

    return ','.join(sorted(switched))


if __name__ == "__main__":
    start = perf_counter()
    print("start")
    print(main())
    print(f"Time taken: {(perf_counter() - start) *1000} miliseconds")
