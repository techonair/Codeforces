"""
cnt = 0
count = [-1]*(10**5 + 1)
we can iterate over the array and check if count[element] == -1
if it is true we cnt++ and store count[element] == cnt
for every query we just print array count[query]
"""

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
l = []

for i in range(m):
    x = int(input())
    l.append(x)

cnt = 0
count = [True]*(10**6)
suffix = [0] * n

for i in range(n-1, -1, -1):
    if count[a[i]] == True:
        cnt += 1
        suffix[i] = cnt
        count[a[i]] = False
    else:
        suffix[i] = cnt
print(suffix)
for i in range(m):
    print(suffix[l[i]-1])