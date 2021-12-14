n = int(input())

arr = [int(i) for i in input().split()]

m = int(input())

quer = [int(i) for i in input().split()]

vasya = 0
petya = 0

flag =  False

arr.sort()

# variables needed for binary search
# -----------------
low = 0
high = len(arr)-1
# -----------------

for i in range(m):
    # Binary Search begins
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == quer[i]:
            index = i
            print('done')
            break
        elif arr[mid] < quer[i]:
            low = mid
        elif arr[mid] > quer[i]:
            high = i

    vasya += index + 1
    petya += n - index
    
print(vasya, petya)