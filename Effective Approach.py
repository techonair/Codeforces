n = int(input())

arr = [int(i) for i in input().split()]

m = int(input())

quer = [int(i) for i in input().split()]

vasya = 0
petya = 0

trr = sorted(arr)

for i in range(m):
    # Binary Search begins
    # variables needed for binary search
    # -----------------
    low = 0
    high = n - 1
    # -----------------
    
    while low <= high:
        mid = (low + high)//2
        
        if quer[i] == trr[mid]:
            index = mid
            
            for i in range(n):
                if arr[i] == trr[mid]:
                    index = i

            vasya += index + 1
            petya += n - index

            break

        elif quer[i] > trr[mid]:
            low = mid + 1
            
        elif quer[i] < trr[mid]:
            high = mid - 1
        
print(vasya, petya)