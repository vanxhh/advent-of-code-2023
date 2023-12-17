from heapq import heappush, heappop

with open("input.txt", "r") as f:
    pattern = [[int(ch) for ch in line] for line in f.read().splitlines()]


def part1():
    answer = 0

    # row, col, row_direction, col_direction, direction_count
    seen = set()

    # heat_loss, row, col, row_direction, col_direction, direction_count
    heap = [(0, 0, 0, 0, 0, 0)]

    while heap:
        heat_loss, row, col, row_direction, col_direction, direction_count = heappop(
            heap
        )

        if row == len(pattern) - 1 and col == len(pattern[0]) - 1:
            answer = heat_loss
            break

        if (row, col, row_direction, col_direction, direction_count) in seen:
            continue

        seen.add((row, col, row_direction, col_direction, direction_count))

        if direction_count < 3 and (row_direction, col_direction) != (0, 0):
            next_row = row + row_direction
            next_col = col + col_direction
            if -1 < next_row < len(pattern) and -1 < next_col < len(pattern[0]):
                heappush(
                    heap,
                    (
                        heat_loss + pattern[next_row][next_col],
                        next_row,
                        next_col,
                        row_direction,
                        col_direction,
                        direction_count + 1,
                    ),
                )

        for next_row_direction, next_col_direction in [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]:
            if (next_row_direction, next_col_direction) != (
                row_direction,
                col_direction,
            ) and (next_row_direction, next_col_direction) != (
                -row_direction,
                -col_direction,
            ):
                next_row = row + next_row_direction
                next_col = col + next_col_direction
                if 0 <= next_row < len(pattern) and 0 <= next_col < len(pattern[0]):
                    heappush(
                        heap,
                        (
                            heat_loss + pattern[next_row][next_col],
                            next_row,
                            next_col,
                            next_row_direction,
                            next_col_direction,
                            1,
                        ),
                    )

    print(answer)


def part2():
    answer = 0

    # row, col, row_direction, col_direction, direction_count
    seen = set()

    # heat_loss, row, col, row_direction, col_direction, direction_count
    heap = [(0, 0, 0, 0, 0, 0)]

    while heap:
        heat_loss, row, col, row_direction, col_direction, direction_count = heappop(
            heap
        )

        if (
            row == len(pattern) - 1
            and col == len(pattern[0]) - 1
            and direction_count >= 4
        ):
            answer = heat_loss
            break

        if (row, col, row_direction, col_direction, direction_count) in seen:
            continue

        seen.add((row, col, row_direction, col_direction, direction_count))

        if direction_count < 10 and (row_direction, col_direction) != (0, 0):
            next_row = row + row_direction
            next_col = col + col_direction
            if -1 < next_row < len(pattern) and -1 < next_col < len(pattern[0]):
                heappush(
                    heap,
                    (
                        heat_loss + pattern[next_row][next_col],
                        next_row,
                        next_col,
                        row_direction,
                        col_direction,
                        direction_count + 1,
                    ),
                )

        if direction_count >= 4 or (row_direction, col_direction) == (0, 0):
            for next_row_direction, next_col_direction in [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0),
            ]:
                if (next_row_direction, next_col_direction) != (
                    row_direction,
                    col_direction,
                ) and (next_row_direction, next_col_direction) != (
                    -row_direction,
                    -col_direction,
                ):
                    next_row = row + next_row_direction
                    next_col = col + next_col_direction
                    if 0 <= next_row < len(pattern) and 0 <= next_col < len(pattern[0]):
                        heappush(
                            heap,
                            (
                                heat_loss + pattern[next_row][next_col],
                                next_row,
                                next_col,
                                next_row_direction,
                                next_col_direction,
                                1,
                            ),
                        )

    print(answer)


part1()
part2()
