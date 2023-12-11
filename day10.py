from collections import deque

with open("input.txt", "r") as f:
    grid = f.read().splitlines()


def part1():
    loop_indices = []

    for row_index, row in enumerate(grid):
        for col_index, tile in enumerate(row):
            if grid[row_index][col_index] == "S":
                initial_row = row_index
                initial_col = col_index

    loop_indices.append((initial_row, initial_col))
    queue = deque()
    queue.append((initial_row, initial_col))

    while queue:
        curr_row, curr_col = queue.popleft()
        curr_char = grid[curr_row][curr_col]

        # Go TOP
        if (
            (curr_row - 1) >= 0
            and curr_char in "S|JL"
            and grid[curr_row - 1][curr_col] in "|7F"
            and ((curr_row - 1, curr_col)) not in loop_indices
        ):
            loop_indices.append((curr_row - 1, curr_col))
            queue.append((curr_row - 1, curr_col))

        # Go LEFT
        if (
            (curr_col - 1) >= 0
            and curr_char in "S-7J"
            and grid[curr_row][curr_col - 1] in "-FL"
            and ((curr_row, curr_col - 1)) not in loop_indices
        ):
            loop_indices.append((curr_row, curr_col - 1))
            queue.append((curr_row, curr_col - 1))

        # Go BOTTOM
        if (
            (curr_row + 1) < len(grid)
            and curr_char in "S|7F"
            and grid[curr_row + 1][curr_col] in "|JL"
            and ((curr_row + 1, curr_col)) not in loop_indices
        ):
            loop_indices.append((curr_row + 1, curr_col))
            queue.append((curr_row + 1, curr_col))

        # Go Right
        if (
            (curr_col + 1) < len(grid[curr_row])
            and curr_char in "S-LF"
            and grid[curr_row][curr_col + 1] in "-7J"
            and ((curr_row, curr_col + 1)) not in loop_indices
        ):
            loop_indices.append((curr_row, curr_col + 1))
            queue.append((curr_row, curr_col + 1))

    print(len(loop_indices) // 2)


part1()
