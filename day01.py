with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def part1():
    answer = 0
    first = ""
    last = ""

    for line in lines:
        first = ""
        last = ""
        for i in line:
            if i.isnumeric():
                if first == "":
                    first = i
                last = i

        answer = answer + int(first + last)

    print(answer)


def part2():
    answer = 0
    list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    first = ""
    last = ""

    for line in lines:
        line = (
            line.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
        )

        for i in line:
            if i.isnumeric():
                if first == "":
                    first = i
                last = i

        answer = answer + int(first + last)
        first = ""
        last = ""

    print(answer)


part1()
part2()
