with open("input.txt", "r") as f:
    image = f.read().splitlines()


def part1():
    answer = 0

    for index, (row1, col1) in enumerate(galaxy_indices):
        for row2, col2 in galaxy_indices[:index]:
            for row in range(min(row1, row2), max(row1, row2)):
                answer += 2 if row in empty_rows else 1
            for col in range(min(col1, col2), max(col1, col2)):
                answer += 2 if col in empty_cols else 1

    print(answer)


def part2():
    answer = 0

    for index, (row1, col1) in enumerate(galaxy_indices):
        for row2, col2 in galaxy_indices[:index]:
            for row in range(min(row1, row2), max(row1, row2)):
                answer += 1000000 if row in empty_rows else 1
            for col in range(min(col1, col2), max(col1, col2)):
                answer += 1000000 if col in empty_cols else 1

    print(answer)


empty_rows = []
for row_index, row in enumerate(image):
    valid = True
    for ch in row:
        if ch != ".":
            valid = False
            break
    if valid:
        empty_rows.append(row_index)

empty_cols = []
for col_index, col in enumerate(zip(*image)):
    valid = True
    for ch in col:
        if ch != ".":
            valid = False
            break
    if valid:
        empty_cols.append(col_index)

galaxy_indices = []
for row_index, row in enumerate(image):
    for col_index, ch in enumerate(row):
        if ch == "#":
            galaxy_indices.append((row_index, col_index))


part1()
part2()
