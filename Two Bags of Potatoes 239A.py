y, k, n = map(int,input().split())

flag = False

x = k - (y%k)

while x+y <= n:
    flag = True
    print(x, end=' ')
    x += k
    
if not flag:
    print(-1)