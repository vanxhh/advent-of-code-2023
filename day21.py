from collections import deque

with open("input.txt") as f:
    grid = f.read().splitlines()

seen = set()
after_n_steps = set()
queue = deque()


def part1():
    for x, line in enumerate(grid):
        for y, ch in enumerate(line):
            if ch == "S":
                seen.add((x, y))
                queue.append((x, y, 64))

    while queue:
        curr_x, curr_y, steps = queue.popleft()

        if steps % 2 == 0:
            after_n_steps.add((curr_x, curr_y))

        if steps == 0:
            continue

        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x = curr_x + x
            next_y = curr_y + y
            if (
                next_x < 0
                or next_x >= len(grid)
                or next_y < 0
                or next_y >= len(grid[0])
                or grid[next_x][next_y] == "#"
                or (next_x, next_y) in seen
            ):
                continue
            seen.add((next_x, next_y))
            queue.append((next_x, next_y, steps - 1))

    print(len(after_n_steps))


part1()
