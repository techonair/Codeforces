n, m = map(int, input().split())

f = list(int(i) for i in input().split())

f.sort()

# formula -> f[k-1+n-1] - f[k-1]

ans = 10**9

for i in range(m-n+1):
    ans = min(ans, f[i+n-1] - f[i])
    print(ans)

print(ans)