def sol(lines):
  answer = 0
  list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  
  first = ""
  last = ""
  
  for line in lines:
    line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
    
    for i in line:
      if i.isnumeric():
        if first == "":
          first = i
        last = i
    
    print(int(first + last))
    answer = answer + int(first + last)
    first = ""
    last = ""
  
  return answer


lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
  
print(sol(lines))