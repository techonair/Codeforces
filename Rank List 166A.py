n, k = map(int, input().split())

arr = []

for i in range(n):
    XY = [int(i) for i in input().split()]
    arr.append(XY)

arr.sort()

# because the keys are in the sorted arr are in ascending rank kth team index -> n-1-k
key1 = arr[n-k][0]
key2 = arr[n-k][1]

low = 0
high = n-1

print(arr)
print(arr[n-k])

while (low <= high):
    m = (low + high) // 2
    print(low, high, m, arr[m][0])
    if arr[m][0] > key1:
        high = m - 1
    elif arr[m][0] < key1:
        low = m + 1
    elif arr[m][0] == key1 and arr[m][1] > key2:
        high = m - 1
    elif arr[m][0] == key1 and arr[m][1] < key2:
        low = m + 1
    elif arr[m][0] == key1 and arr[m][1] == key2:
        if (m != 0 and arr[m-1][0] != key1 and arr[m-1][1] != key2) or (m != 0 and arr[m-1][0] != key1 and arr[m-1][1] == key2):
            first_occurence = m
            break
        elif m == 0:
            first_occurence = m
            break
        else:
            high = m - 1

low = first_occurence
high = n-1

while (low <= high):
    m = (low + high) // 2
    if arr[m][0] > key1:
        high = m - 1
    elif arr[m][0] < key1:
        low = m + 1
    elif arr[m][0] == key1 and arr[m][1] > key2:
        high = m - 1
    elif arr[m][0] == key1 and arr[m][1] < key2:
        low = m + 1
    elif arr[m][0] == key1 and arr[m][1] == key2:
        if (m != n-1 and arr[m+1][0] != key1 and arr[m+1][1] != key2) or (m != n-1 and arr[m+1][0] != key1 and arr[m+1][1] == key2):
            last_occurence = m
            break
        elif m == n-1:
            last_occurence = m
            break
        else:
            low = m + 1

print(last_occurence - first_occurence + 1)