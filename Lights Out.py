# Storing input in 3x3 matrix

grid = []

for i in range(3):
    grid.append(list(map(int, input().split())))

# Making a 5x5 null matirx

row, column = 5,5

arr = [[0 for i in range(column)] for j in range(row)]

# Handling edge cases 
# modifying null matrix to fit the grid matrix in the center

for i in range(1,4):
    for j in range(1,4):
        arr[i][j] = grid[i-1][j-1]

"""
print('Input Grid')
for ro in grid:
    print(ro)

print('Initial arr')

for ro in arr:
    print(ro)

"""

# if the sum of the element and its nearest neighbor elements is 1 
# then the light at that element will be OFF '0'
# else it will be ON '1'

for i in range(1,4):
    for j in range(1,4):
        if sum([arr[i][j-1], arr[i][j+1], arr[i-1][j], arr[i+1][j]], arr[i][j]) % 2:
            print('0', end='')
        else:
            print('1', end='')
    print()