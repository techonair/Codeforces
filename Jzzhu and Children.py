import math

children, candies = input().split()

line = list(int(i) for i in input().split())

max = 0
last = 0

for i in range(int(children)):

    var = math.ceil(line[i]/int(candies))

    if var >= max:
        max = math.ceil(line[i]/int(candies))
        last = i+1

print(last)

