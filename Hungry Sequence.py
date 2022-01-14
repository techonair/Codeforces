n = int(input())

for i in range(1, n+1):
    print(n+i, end= " ")

"""
n = int(input())

isPrimes = [True] * ((10**6)+1)
isPrimes[1] = False

count = 0

for i in range(2, 10**3):
    if count > n-1:
        break
    else:
        if isPrimes[i]:
            print(i, end=" ")
            count += 1
            for j in range(i, 10**3):
                isPrimes[i*j] = False
"""