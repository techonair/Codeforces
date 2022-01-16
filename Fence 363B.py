n, k = map(int, input().split())

arr = [int(i) for i in input().split()]

first = 0

for i in range(k):
    first += arr[i]

window = first
j = 1
for i in range(1, n-k+1):
    first = first - arr[i-1] + arr[i-1+k]
    if first < window:
        window = first
        j = i+1

print(j)