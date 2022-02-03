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
