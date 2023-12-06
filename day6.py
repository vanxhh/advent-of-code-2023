import operator
import functools

with open("input.txt", "r") as f:
    input = f.read()


def part1(input):
    time, dist = input.splitlines()

    race_times = list(map(int, time.split(": ")[1].split()))
    race_dists = list(map(int, dist.split(": ")[1].split()))

    valid_holds = [0] * len(race_times)

    for id, race_time in enumerate(race_times):
        for i in range(1, race_time + 1):
            temp = (race_time - i) * i
            if temp > race_dists[id]:
                valid_holds[id] += 1

    answer = functools.reduce(operator.mul, valid_holds, 1)
    print(answer)


def part2(input):
    time, dist = input.splitlines()

    race_time = int(time.split(": ")[1].replace(" ", ""))
    race_dist = int(dist.split(": ")[1].replace(" ", ""))

    def check(num):
        return num * (race_time - num)

    hi = race_time // 2
    lo = 0

    if check(hi) < race_dist:
        print(0)
        return

    while lo + 1 < hi:
        print(lo, hi)
        mid = (lo + hi) // 2
        if check(mid) >= race_dist:
            hi = mid
        else:
            lo = mid

    first = hi
    last = int(race_time - first)

    print(last - first + 1)


part2(input)
