n = int(input())

arr = [int(i) for i in input().split()]

# noticed that if a number in the array occurs more than half of the size of the array
# that is arr.count(arr[i]) > (n+1) / 2
# then it is impossible that the array elements will ever have distinct neighbours

flag = True

for i in range(n):
    cnt = arr.count(arr[i])
    if cnt > (n+1) / 2:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
