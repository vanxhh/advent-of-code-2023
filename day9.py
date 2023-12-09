with open("input.txt", "r") as f:
    input = [[int(val) for val in line.split()] for line in f.read().splitlines()]


def helper1(sequence):
    new_sequence = [0] * (len(sequence) - 1)

    if sequence == [0] * len(sequence):
        sequence.append(0)
        return sequence

    for value_idx in range(len(sequence) - 1):
        new_sequence[value_idx] = sequence[value_idx + 1] - sequence[value_idx]

    last_value = new_sequence[-1]
    new_new_sequence = helper1(new_sequence)
    new_sequence.append(last_value + new_new_sequence[-1])
    return new_sequence


def part1():
    answer = []

    for sequence in input:
        answer.append(helper1(sequence)[-1] + sequence[-1])

    print(sum(answer))


def helper2(sequence):
    new_sequence = [0] * (len(sequence) - 1)

    if sequence == [0] * len(sequence):
        sequence.insert(0, 0)
        return sequence

    for value_idx in range(len(sequence) - 1):
        new_sequence[value_idx] = sequence[value_idx + 1] - sequence[value_idx]

    first_value = new_sequence[0]
    new_new_sequence = helper2(new_sequence)
    new_sequence.insert(0, first_value - new_new_sequence[0])
    return new_sequence


def part2():
    answer = []

    for sequence in input:
        answer.append(sequence[0] - helper2(sequence)[0])

    print(sum(answer))


part1()
part2()
