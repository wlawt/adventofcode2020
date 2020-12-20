inputs = open("day3.txt", "r")

data = []
for row in inputs:
  data.append(row.strip("\n"))

idx = 0
trees = 0
for row in range(1, len(data)):
  idx += 3
  if data[row][idx] == '#':
    trees += 1

print(trees)