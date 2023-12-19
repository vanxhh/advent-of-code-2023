with open("input.txt", "r") as f:
    block1, block2 = f.read().split("\n\n")
    parts = []
    workflows = {}

    for line in block1.splitlines():
        workflow, rest = line.split("{")
        rules = rest[:-1].split(",")
        workflows[workflow] = ([], rules[-1])

        for rule in rules[:-1]:
            comparison, target = rule.split(":")
            key = comparison[0]
            operator = comparison[1]
            num = int(comparison[2:])
            workflows[workflow][0].append((key, operator, num, target))

    for line in block2.splitlines():
        item = {}
        for segment in line[1:-1].split(","):
            ch, n = segment.split("=")
            item[ch] = int(n)
        parts.append(item)


def test_accepted(part, target):
    if target == "R":
        return False

    if target == "A":
        return True

    for condition in workflows[target][0]:
        key, operator, num, next_target = condition
        if operator == ">":
            if part[key] > num:
                return test_accepted(part, next_target)
        else:
            if part[key] < num:
                return test_accepted(part, next_target)

    return test_accepted(part, workflows[target][1])


def part1():
    answer = 0
    for part in parts:
        if test_accepted(part, "in"):
            for key in part:
                answer += part[key]
    print(answer)


def test_ranges(ranges, target):
    if target == "R":
        return 0

    if target == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product

    total = 0

    for condition in workflows[target][0]:
        key, operator, num, next_target = condition
        lo, hi = ranges[key]

        if operator == "<":
            accepted_range = (lo, num - 1)
            rejected_range = (num, hi)
        else:
            accepted_range = (num + 1, hi)
            rejected_range = (lo, num)

        if accepted_range[0] <= accepted_range[1]:
            new_ranges = dict(ranges)
            new_ranges[key] = accepted_range
            total += test_ranges(new_ranges, next_target)
        if rejected_range[0] <= rejected_range[1]:
            ranges[key] = rejected_range

    total += test_ranges(ranges, workflows[target][1])
    return total


def part2():
    answer = test_ranges({key: (1, 4000) for key in "xmas"}, "in")
    print(answer)


part1()
part2()
