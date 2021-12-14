n, m = input().split()

h = [int(i) for i in input().split()]

count = 0
i = 0
while i < int(m):
    for j in range(1, int(m)):
        if j>i:
            i = i+1
        elif j<=i:
            count += int(n) - h[i-1] + j
            i = i+1

print(count)