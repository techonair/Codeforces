n = int(input())
arr = [int(i) for i in input().split()]
i = 1

while i < n and arr[i-1] < arr[i]:
    i += 1

j = i

while j < n and arr[j-1] > arr[j]:
    j += 1

s = arr[:i-1] + arr[i-1:j][::-1] + arr[j:]
print(s)
q = sorted(arr)

if s == q:
    print('yes')
    print(i, j)

else:
    print('no')
