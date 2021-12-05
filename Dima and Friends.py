n = int(input())

friends = list(input().split())

sum = 0

for i in friends:
    sum += int(i)

ways = 0

for i in range(1,6):
    if (sum+i)%(n+1) != 1:
        ways += 1

print(ways)
