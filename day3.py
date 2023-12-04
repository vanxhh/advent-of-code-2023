import re
import itertools
from collections import defaultdict
import math

with open("input.txt", "r") as f:
  lines = f.read().split()
  
def sol(lines):
  answer = 0
  
  coordList = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
  
  gears = defaultdict(list)
  
  for i, line in enumerate(lines):
    for match in re.finditer("\d+", line):
      valid = False
      num = int(match.group())
      visited = set()
      
      for j in range(match.start(), match.end()):
        for coord in coordList:
          x = i + coord[0]
          y = j + coord[1]
          
          if x > -1 and y > -1 and x < len(line) and y < len(lines):
            if (x, y) not in visited:
              test = lines[x][y]
              if test != "." and not test.isdigit():
                if test == "*":
                  gears[(x, y)].append(num)
                valid = True
              visited.add((x, y))
      
      if valid:
        answer += num

  print(answer)
  
  answer2 = sum(math.prod(value) for value in gears.values() if len(value) == 2)
  print(answer2)

sol(lines)
  