n = int(input())

n = int(input())

arr = input()

a = sorted(arr[0:n])
b = sorted(arr[n:])

if a > b:
    a, b = b, a

for i in range(n):
    if a[i] >= b[i]:
        print('NO')
        break
else:
    print('YES')


"""
arr = [int(i) for i in input()]

flag = False

if arr[0] <= arr[2*n-1]:
    for i in range(0, n):
        if arr[i] <= arr[(2*n-1-i)]:
            flag = True
        else:
            flag = False
            break

if arr[0] >= arr[2*n-1] and flag == False:
    for i in range(0, n):
        if arr[i] >= arr[(2*n-1-i)]:
            flag = True
        else:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')


"""
