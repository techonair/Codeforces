n = int(input())

a = 10**9
b = -10**9

arr1 = []
arr2 = []

flag = False

for i in range(n):
    x, y = map(int, input().split())
    arr1.append(x)
    arr2.append(y)
    a = min(a, x)
    b = max(b, y)

for i in range(n):
    if arr1[i] == a and arr2[i] == b:
        print(i+1)
        flag = True
        break

if not flag:
    print(-1)