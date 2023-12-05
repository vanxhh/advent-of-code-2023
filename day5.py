import re

with open("input.txt", "r") as f:
    input = f.read()


def sol(input):
    parts = input.split("\n\n")

    seeds = [int(seed) for seed in parts[0].split(":")[1].split()]

    others = parts[1:]

    map_list = []

    for map in others:
        map_list.append(map.split(":\n")[1].split("\n"))

    ans_list = []

    for seed in seeds:
        temp = seed
        for map in map_list:
            for map_line in map:
                dest, src, size = map_line.split()
                dest = int(dest)
                src = int(src)
                size = int(size)
                if temp in range(src, src + size):
                    temp = dest + (temp - src)
                    break

        ans_list.append(temp)

    print(min(ans_list))


sol(input)
