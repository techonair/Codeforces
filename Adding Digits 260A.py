a, b, n = map(int, input().split())
flag = False
for i in range(10):
    new = str(a) + str(i)
    if int(new) % b == 0:
        flag = True
        break

if flag:
    if n > 1:
        print(new+ '0'*(n-1))
    else:
        print(new)
else:
    print(-1)