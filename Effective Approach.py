n = int(input())

idx = [0]*(n+1)

arr = [int(i) for i in input().split()]

m = int(input())

quer = [int(i) for i in input().split()]

for i in range(n):
    idx[arr[i]] = i+1

vasya = 0
petya = 0
for q in quer:
    vasya += idx[q]
    petya += n-idx[q]+1

print(vasya, petya)

# Time complexity of above code O(n+m)
# Time complexity of below code O(n*m)
"""
n = int(input())

arr = [int(i) for i in input().split()]

m = int(input())

quer = [int(i) for i in input().split()]

vasya = 0
petya = 0

idx = [0]*(n+1)

for i in range(m):
    if idx[quer[i]-1] != 0:
        vasya += idx[quer[i]-1] + 1
        petya += n - idx[quer[i]-1]
    else:
        for j in range(n):
            if arr[j] == quer[i]:
                idx[quer[i]-1] == j
                vasya += j+1
                petya += n-j

print(vasya, petya)
"""