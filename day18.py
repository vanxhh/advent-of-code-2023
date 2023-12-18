with open("input.txt") as f:
    instructions = f.read().splitlines()


def part1():
    path_points = [(0, 0)]
    path_count = 0

    for instruction in instructions:
        curr = path_points[-1]
        direction, steps, _ = instruction.split()
        steps = int(steps)

        if direction == "R":
            path_points.append((curr[0], curr[1] + steps))
        elif direction == "L":
            path_points.append((curr[0], curr[1] - steps))
        elif direction == "U":
            path_points.append((curr[0] - steps, curr[1]))
        elif direction == "D":
            path_points.append((curr[0] + steps, curr[1]))

        path_count += steps

    area = 0

    for index in range(len(path_points)):
        area += path_points[index][0] * (
            path_points[index - 1][1] - path_points[(index + 1) % len(path_points)][1]
        )

    area = abs(area) // 2

    interior_points = area - path_count // 2 + 1

    answer = interior_points + path_count
    print(answer)


def part2():
    path_points = [(0, 0)]
    path_count = 0

    for instruction in instructions:
        curr = path_points[-1]
        _, _, code = instruction.split()

        code = code[2:-1]
        direction = code[-1]
        steps = int(code[:-1], 16)

        # right
        if direction == "0":
            path_points.append((curr[0], curr[1] + steps))
        # down
        elif direction == "1":
            path_points.append((curr[0] + steps, curr[1]))
        # left
        elif direction == "2":
            path_points.append((curr[0], curr[1] - steps))
        # up
        elif direction == "3":
            path_points.append((curr[0] - steps, curr[1]))

        path_count += steps

    area = 0

    for index in range(len(path_points)):
        area += path_points[index][0] * (
            path_points[index - 1][1] - path_points[(index + 1) % len(path_points)][1]
        )

    area = abs(area) // 2

    interior_points = area - path_count // 2 + 1

    answer = interior_points + path_count
    print(answer)


part1()
part2()
