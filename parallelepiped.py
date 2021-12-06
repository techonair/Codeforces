area = list(int(i) for i in input().split())

sum = 0

for i in area:
    if i == min(area):
        sum += i*4
    else:
        sum += i

print(sum)

# Solution is not right