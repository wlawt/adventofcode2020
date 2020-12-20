inputs = open("day1.txt", "r")

data = []
for n in inputs:
  data.append(int(n.strip('\n')))

data.sort()

res = []

for curr in range(len(data)):
  for next in range(curr+1, len(data)):
    for third in range(curr+2, len(data)):
      if data[curr] + data[next] + data[third] == 2020:
        res.append(data[curr] * data[next] * data[third])

print(max(res))
