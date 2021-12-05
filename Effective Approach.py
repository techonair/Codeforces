n = int(input())

arr = [int(i) for i in input().split()]

m = int(input())

quer = [int(i) for i in input().split()]

vasya = 0
petya = 0

"""
for i in range(m):
    for j in range(n):
        if quer[i] != arr[j]:
            vasya += 1
        elif quer[i] == arr[j]:
            vasya += 1
            petya += n - j 
            break
"""
print(vasya, petya)