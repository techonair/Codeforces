n = int(input())

count = 0

for i in range(n):
    sure = list(int(i) for i in input().split())
    sum = 0
    for i in sure:
        sum += i
    if sum >= 2:
        count += 1

print(count)