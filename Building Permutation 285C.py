n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
ans = 0
for i in range(n):
    ans += abs(i+1-arr[i])

print(ans)