from collections import deque

with open("input.txt", "r") as f:
    layout = f.read().splitlines()


def find_tiles(row, col, d_row, d_col):
    start = (row, col, d_row, d_col)
    travelled_spaces = set()
    queue = deque()
    queue.append(start)

    while queue:
        (row, col, d_row, d_col) = queue.popleft()

        row += d_row
        col += d_col

        if row < 0 or row >= len(layout) or col < 0 or col >= len(layout[0]):
            continue

        ch = layout[row][col]

        if ch == "." or (ch == "|" and d_col == 0) or (ch == "-" and d_row == 0):
            if (row, col, d_row, d_col) not in travelled_spaces:
                travelled_spaces.add((row, col, d_row, d_col))
                queue.append((row, col, d_row, d_col))

        elif ch == "/":
            d_row, d_col = -d_col, -d_row
            if (row, col, d_row, d_col) not in travelled_spaces:
                travelled_spaces.add((row, col, d_row, d_col))
                queue.append((row, col, d_row, d_col))

        elif ch == "\\":
            d_row, d_col = d_col, d_row
            if (row, col, d_row, d_col) not in travelled_spaces:
                travelled_spaces.add((row, col, d_row, d_col))
                queue.append((row, col, d_row, d_col))

        else:
            for d_row, d_col in [(-1, 0), (1, 0)] if ch == "|" else [(0, -1), (0, 1)]:
                if (row, col, d_row, d_col) not in travelled_spaces:
                    travelled_spaces.add((row, col, d_row, d_col))
                    queue.append((row, col, d_row, d_col))

    unique_travelled_spaces = set((row, col) for (row, col, _, _) in travelled_spaces)
    return len(unique_travelled_spaces)


def part1():
    print(find_tiles(0, -1, 0, 1))


def part2():
    max_energized_tiles = 0

    for row in range(len(layout)):
        max_energized_tiles = max(max_energized_tiles, find_tiles(row, -1, 0, 1))
        max_energized_tiles = max(
            max_energized_tiles, find_tiles(row, len(layout[0]), 0, -1)
        )

    for col in range(len(layout[0])):
        max_energized_tiles = max(max_energized_tiles, find_tiles(-1, col, 1, 0))
        max_energized_tiles = max(
            max_energized_tiles, find_tiles(len(layout), col, -1, 0)
        )

    print(max_energized_tiles)


part1()
part2()
