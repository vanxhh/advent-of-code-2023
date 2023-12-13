with open("input.txt", "r") as f:
    patterns = [line.split() for line in f.read().split("\n\n")]


def check_mirror(pattern):
    for row in range(1, len(pattern)):
        above_mirror = pattern[:row][::-1]
        below_mirror = pattern[row:]

        above_mirror = above_mirror[: len(below_mirror)]
        below_mirror = below_mirror[: len(above_mirror)]

        if above_mirror == below_mirror:
            return row

    return 0


def check_mirror_with_smudge(pattern):
    for row in range(1, len(pattern)):
        above_mirror = pattern[:row][::-1]
        below_mirror = pattern[row:]

        above_mirror = above_mirror[: len(below_mirror)]
        below_mirror = below_mirror[: len(above_mirror)]

        diff_char_count = 0

        for row1, row2 in zip(above_mirror, below_mirror):
            for char1, char2 in zip(row1, row2):
                if char1 != char2:
                    diff_char_count += 1

        if diff_char_count == 1:
            return row

    return 0


def sol():
    part1 = 0
    part2 = 0

    for pattern in patterns:
        part1 += check_mirror(pattern) * 100 + check_mirror(list(zip(*pattern)))
        part2 += check_mirror_with_smudge(pattern) * 100 + check_mirror_with_smudge(
            list(zip(*pattern))
        )

    print(part1)
    print(part2)


sol()
