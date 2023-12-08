# sourcery skip: avoid-builtin-shadow
with open("input.txt", "r") as f:
    input = f.read()

strength = {"A": "E", "K": "D", "Q": "C", "J": "B", "T": "A"}

plays = []


def sol(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        return 4 if 2 in counts else 3
    if counts.count(2) == 4:
        return 2
    return 1 if 2 in counts else 0


for line in input.splitlines():
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(
    key=lambda play: (
        sol(play[0]),
        [strength.get(card, card) for card in play[0]],
    )
)

answer = sum((rank + 1) * tuple[1] for rank, tuple in enumerate(plays))
print(answer)
