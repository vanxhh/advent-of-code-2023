# sourcery skip: avoid-builtin-shadow
with open("input.txt", "r") as f:
    input = f.read()

letter_map = {"A": "E", "K": "D", "Q": "C", "J": ".", "T": "A"}

plays = []


def score(hand):
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


def replaceJokerInHand(hand):
    if hand == "":
        return [""]

    return [
        replace + rest
        for replace in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for rest in replaceJokerInHand(hand[1:])
    ]


def findMaxOfPermutations(hand):
    return max(map(score, replaceJokerInHand(hand)))


def strength(hand):
    return (findMaxOfPermutations(hand), [letter_map.get(card, card) for card in hand])


for line in input.splitlines():
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(key=lambda play: strength(play[0]))

part2 = sum((rank + 1) * tuple[1] for rank, tuple in enumerate(plays))
print(part2)
