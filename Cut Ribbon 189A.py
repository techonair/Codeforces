n, a, b, c = map(int, input().split())

"""
# As after cutting there can be
# x number of 'a' sized ribbons, 
# y number of 'b' sized ribbons, and
# z number of 'c' sized ribbons
# if we sum up all pieces we have then we will get 'n'
# therefore if we maximize ax+by+cz then we can get the answer which is x+y+z
# we can iterate over values of x and y from 0 to 4000 and find values of z 
# using eq. ax+by+cz for which answer is maximum
# x, y, or z can have max value 4000 and min value '0'
# (because, 1 <= n,a,b,c,d <= 4000)(positive values)

maximum = 0

for i in range(0, n+1):
    for j in range(0, n+1):
        x, y = i, j
        z = (n - a*x - b*y) / c
        if z < 0 :
            break
        if int(z) == z:
            maximum = max(maximum, x + y + int(z))

print(maximum)
"""

f=[0]+[-5000]*4000
for i in range(1,n+1):
    print('Before:', f[i], f[i-a], f[i-b], f[i-c])
    f[i]=max(f[i-a],f[i-b],f[i-c])+1
    print('After:', f[i], f[i-a], f[i-b], f[i-c])
    if i == 5:
        break

print(f[i])

link: https://codeforces.com/contest/189/status/A/page/6?order=BY_PROGRAM_LENGTH_ASC