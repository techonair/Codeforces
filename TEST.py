n = int(input())

s = [int(i) for i in input().split()]
d = {}
for i in range(n):
    a = s[i]
    if a not in d:
        d[a] = (i,0)
    else:
        d[a] = (i, -1 if d[a][1] and i - d[a][0] != d[a][1] else i - d[a][0])
b = [(i,d[i][1]) for i in sorted(d.keys()) if d[i][1] >= 0]
print(len(b))
for i in b:
    print(i[0],i[1])