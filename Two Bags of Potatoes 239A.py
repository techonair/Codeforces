y, k, n = map(int,input().split())

start = 1

if y < k:
    start = y

flag = False

for i in range(start, n+1):
    if (i + y) <= n:
        if (i + y) % k == 0:
            flag = True
            print(i, end=' ')
    else:
        break

if not flag:
    print(-1)