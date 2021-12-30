n, m = map(int, input().split())

f = list(int(i) for i in input().split())

f.sort()

# formula -> f[i+n-1] - f[i]

ans = 10**9

for i in range(m-n+1):
    ans = min(ans, f[i+n-1] - f[i])

print(ans)