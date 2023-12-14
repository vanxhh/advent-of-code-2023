with open("input.txt") as f:
    text = tuple(tuple(line) for line in f.read().splitlines())


def tilt():
    global text

    text = tuple(list(line) for line in text)
    text = tuple(zip(*text))
    text = tuple(list(line) for line in text)

    for line in text:
        for i in range(1, len(line)):
            if line[i] == "O":
                j = i - 1
                k = i
                while j >= 0:
                    if line[j] == ".":
                        line[k], line[j] = line[j], line[k]
                    if line[j] == "#":
                        break
                    j -= 1
                    k -= 1


def part1():
    global text

    tilt()
    text = tuple(list(line) for line in text)
    text = tuple(zip(*text))

    answer = 0
    for row_index, row in enumerate(text):
        answer += row.count("O") * (len(row) - row_index)
    print(answer)


def part2():
    global text

    iterations = 0
    seen = {text}
    states = [text]

    def cycle():
        global text

        for _ in range(4):
            tilt()
            text = tuple(tuple(row[::-1]) for row in text)

    while True:
        iterations += 1
        cycle()

        if text in seen:
            break
        seen.add(text)
        states.append(text)

    outside_cycle = states.index(text)

    text = states[
        (1000000000 - outside_cycle) % (iterations - outside_cycle) + outside_cycle
    ]

    answer = 0
    for row_index, row in enumerate(text):
        answer += row.count("O") * (len(row) - row_index)
    print(answer)


part1()
part2()
