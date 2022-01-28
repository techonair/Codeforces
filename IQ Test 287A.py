matrix = [[j for j in input()] for _ in range(4)]

# iterating over just 2nd row, 3rd row, and 4th row can give answer
flag = False

for i in range(1,4):
    for j in range(0,3):
        count_dot = 0
        count_hash = 0
        var = matrix[i][j]
        for x in range(i-1, i+1):
            for y in range(j, j+2):
                if matrix[x][y] == '#':
                    count_hash += 1
                elif matrix[x][y] == '.':
                    count_dot += 1
                if count_hash == 3 or count_dot == 3:
                    flag = True
                    break
        if flag:
            break
    if flag:
        break

if flag:
    print('YES')
else:
    print('NO')