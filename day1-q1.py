def sol(lines):

  answer = 0
  first = ""
  last = ""

  for line in lines:
    first = ""
    last = ""
    for i in line:
      if i.isnumeric():
        if first == "":
          first = i
        last = i

    answer = answer + int(first + last)

  return answer

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
  
print(sol(lines))