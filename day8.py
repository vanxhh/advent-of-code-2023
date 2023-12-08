from collections import defaultdict
from math import gcd

# sourcery skip: avoid-builtin-shadow
with open("input.txt", "r") as f:
    input = f.read()


def sol1():
    current = "AAA"
    inst = instructions
    steps = 0

    while current != "ZZZ":
        current = maps[current][0 if inst[0] == "L" else 1]
        inst = inst[1:] + inst[0]
        steps += 1

    print(steps)


def sol2():  # sourcery skip: avoid-builtin-shadow
    cycles = []

    starts = [
        line.split(" = ")[0]
        for line in lines.splitlines()
        if line.split(" = ")[0][-1] == "A"
    ]

    for position in starts:
        curr_instructions = instructions

        count = 0
        first_z_found = None

        while True:
            while position[-1] != "Z":
                count += 1
                position = maps[position][0 if curr_instructions[0] == "L" else 1]
                curr_instructions = curr_instructions[1:] + curr_instructions[0]

            if first_z_found is None:
                first_z_found = position
                cycles.append(count)
                count = 0
            elif position == first_z_found:
                break

    part2 = cycles.pop()

    for num in cycles:
        part2 = part2 * num // gcd(part2, num)

    print(part2)


instructions, lines = input.split("\n\n")

maps = defaultdict(tuple)
for line in lines.splitlines():
    maps[line.split(" = ")[0]] = tuple(line.split(" = ")[1][1:-1].split(", "))

sol1()
sol2()
