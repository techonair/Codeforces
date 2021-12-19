n = int(input())

if n%2 == 0:
    # print(*list(range(n, 0, -1)))
    for i in range(2, n+1, 2):
        print(i, i -1, end = ' ')
else: 
    print(-1)