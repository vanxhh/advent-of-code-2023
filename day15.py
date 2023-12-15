with open("input.txt", "r") as f:
    instructions = f.read()


def find_hash(str):
    hash_value = 0
    for ch in str:
        hash_value += ord(ch)
        hash_value *= 17
        hash_value %= 256
    return hash_value


def part1():
    answer = 0
    for instruction in instructions.split(","):
        answer += find_hash(instruction)
    print(answer)


def part2():
    boxes = [[] for _ in range(256)]
    focal_lengths = {}

    for instruction in instructions.split(","):
        if "=" in instruction:
            label, focal_length = instruction.split("=")
            hash_value = find_hash(label)
            focal_lengths[label] = int(focal_length)

            if label not in boxes[hash_value]:
                boxes[hash_value].append(label)

        if "-" in instruction:
            label = instruction[:-1]
            hash_value = find_hash(label)

            if label in boxes[hash_value]:
                boxes[hash_value].remove(label)

    answer = 0
    for box_index, box in enumerate(boxes):
        for lens_index, lens in enumerate(box):
            answer += (box_index + 1) * (lens_index + 1) * focal_lengths[lens]
    print(answer)


part1()
part2()
