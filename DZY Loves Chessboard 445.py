"""
n, m = map(int, input().split())

# input matrix

matrix = []

for i in range(n):
    matrix.append(list(j for j in input()))

# building a real chess board like layout with 'B' and 'W'

grid = []

for i in range(m):
    ls=[]
    for j in range(n):
        if (i+j)%2 ==0:
            ls.append('B')
        else:
            ls.append('W')
    grid.append(ls)

# replacing letters 'B' and 'W' from the bad cells by '-'

for i in range(m):
    for j in range(n):
        if matrix[i][j] == '-':
            grid[i][j] = '-'

# printing the grid elements

for i in range(m):
    for j in range(n):
        print(grid[i][j], end= '')
    print('')

print('T H E   E N D')

"""

n,m=map(int,input().split())

chess=['W','B']

for i in range(n):
	grid = list(input())

	for j in range(m):
		if grid[j] == '.':
			grid[j] = chess[(i+j)%2]

	print(''.join(grid))