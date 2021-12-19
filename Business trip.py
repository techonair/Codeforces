n = int(input())
l = [int(i) for i in input().split()]

l.sort()
sum = 0
months = 0

for i in range(len(l)-1, -1, -1):
    if sum < n:
        sum += l[i]
        months += 1
    else:
        break

if sum >= n:
    print(months)
else:
    print(-1)