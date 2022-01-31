n, m, d = map(int, input().split())

matrix = [[int(j) for j in input().split()] for _ in range(n)]

mid = matrix[n//2][m//2]
sum = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] != mid:
            sum += mid % matrix[i][j] + d
            print(sum)

print(sum)