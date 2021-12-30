n = int(input())

f = [int(i) for i in input().split()]

f.sort()

min = f[0]
max = f[n-1]

count_min_max = 0

# wrong/use combinatronics
for i in f:
    if i == min or i == max:
        count_min_max += 1

print(max-min, count_min_max)