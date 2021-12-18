n, m = map(int, input().split())

ran = range(32)

print(sum(a*a + b - n == a + b*b -m == 0 for a in ran for b in ran))

# to keep in mind
# 0 <= b <= n
# 0 <= a <= m

"""
for a in range(int(n)+1):
    for b in range(int(m)+1):
        if a**2 + b == int(n) and a + b**2 == int(m):
            count += 1
            #print(a, b)

print(count)
"""