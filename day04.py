with open("input.txt", "r") as f:
  cards = f.read().split("\n")
  
def sol(cards):
  answer1 = 0
  scratchcards = [1] * len(cards)
  
  for i, card in enumerate(cards):
    numbers = card.split(": ")[1]
    winning = numbers.split(" | ")[0].split()
    owned = numbers.split(" | ")[1].split()
    
    score = 0
    matches = 0
    for num in owned:
      if num in winning:
        matches += 1
        if score == 0:
          score = 1
        else:
          score *= 2
    
    answer1 += score
    
    for match in range(matches):
      scratchcards[i + match + 1] += scratchcards[i]
    
  print(answer1)
  answer2 = sum(scratchcards)
  print(answer2)

sol(cards)