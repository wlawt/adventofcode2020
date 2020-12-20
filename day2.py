inputs = open("day2.txt", "r")

data = []
for n in inputs:
  data.append(n.strip('\n'))

valid = 0
for d in data:
  res = d.split(" ")

  low, high = res[0].split("-")

  char = res[1][0]

  pwd = res[2]

  first = False
  second = False
  for n, c in enumerate(pwd, 1):
    if n == int(low) and c == char:
      first = True
    
    if n == int(low) and c != char:
      continue

    if n == int(high) and c == char:
      second = True

    if n == int(high) and c != char:
      seocnd = True
     
  #print(first, second, low, high)
  if not first and second:
    valid += 1
  elif first and not second:
    valid += 1

  
  #if counter >= int(low) and counter <= int(high):
   
print(valid)