with open("input.txt") as f:
    records = [
        [line.split()[0], tuple(map(int, line.split()[1].split(",")))]
        for line in f.read().splitlines()
    ]

# memoization for efficiency
seen = {}


def combinations(springs, arrangement):
    if arrangement == ():
        return 1 if "#" not in springs else 0

    if springs == "":
        return 1 if arrangement == () else 0

    key = (springs, arrangement)

    if key in seen:
        return seen[key]

    valid_combinations = 0

    # treat the unknown spring as a '.'
    if springs[0] in ".?":
        valid_combinations += combinations(springs[1:], arrangement)

    # treat the unknown spring as a '#'
    if springs[0] in "#?":
        if (
            arrangement[0] <= len(springs)
            and "." not in springs[: arrangement[0]]
            and (arrangement[0] == len(springs) or springs[arrangement[0]] != "#")
        ):
            valid_combinations += combinations(
                springs[arrangement[0] + 1 :], arrangement[1:]
            )

    seen[key] = valid_combinations
    return valid_combinations


def part1():
    answer = 0

    for springs, arrangement in records:
        answer += combinations(springs, arrangement)

    print(answer)


def part2():
    answer = 0

    for springs, arrangement in records:
        springs = "?".join([springs] * 5)
        arrangement *= 5
        answer += combinations(springs, arrangement)

    print(answer)


part1()
part2()
