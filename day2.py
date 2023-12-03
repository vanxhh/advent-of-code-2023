def sol(lines):
  answer1 = 0
  answer2 = 0
  optimal = {
    "red": 12,
    "green": 13,
    "blue": 14
  }
  
  for line in lines:
    valid = True
    id, sets = line.split(": ")
    
    dict = {
      "red": 0,
      "green": 0,
      "blue": 0
    }
    
    for set in sets.split("; "):
      for cubes in set.split(", "):
        num, color = cubes.split(" ")
        num = int(num)
        dict[color] = max(dict[color], num)
        if num > optimal.get(color, 0):
          valid = False
    
    score = 1
    for item in dict.values():
      score *= item
    
    answer2 += score
     
    if valid:
      answer1 += int(id.split(" ")[-1])
      
  print(answer1)
  print(answer2)

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
  
sol(lines)