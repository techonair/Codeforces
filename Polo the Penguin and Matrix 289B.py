# Step 1: checking if all elements have same mod values with d
#         a[i] % d should be equal for all
# Step 2: Sort array
#         Minimum will be when we make all elements equals to middle element

n, m, d = map(int, input().split())

arr = []
remainder = -1
flag = True

for _ in range(n):
    for i in input().split():
        arr.append(int(i))
        temp = int(i) % d
        if remainder == -1:
            remainder = temp
        elif remainder != -1 and temp != remainder:
            flag = False
            break
    if flag == False:
        break

if flag:
    arr.sort()
    k = n*m
    sum_mod = 0
    mid = arr[int(k/2)]
    for i in range(k):
        sum_mod += abs(arr[i] - mid)

if flag:
    print(int(sum_mod/d))
else:
    print(-1)