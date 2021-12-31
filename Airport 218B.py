n, m =  map(int, input().split())

planes = [int(i) for i in input().split()]

temp_1 = planes[:]

maximum = 0
minimum = 0

# commented code has high time complexity but logic is same
"""
while n > 0:
    maxX = 0
    for i in range(m):
        if temp_1[i] > temp_1[maxX]:
            maxX = i
    maximum += temp_1[maxX]
    temp_1[maxX] -= 1      

    mini = 0
    for j in range(m):
        if temp_2[mini] == 0:
            mini = mini +1
            if mini < m  and temp_2[j] <= temp_2[mini]:
                mini = j
            else:
                mini = mini-2
        elif temp_2[j] > 0 and temp_2[j] < temp_2[mini]:
            mini = j
    minimum += temp_2[mini]
    temp_2[mini] -= 1

    n -= 1

print(maximum, minimum)
"""

for i in range(n):
    temp_1.sort()
    maximum += temp_1[m-1]
    temp_1[m-1] -= 1

    planes.sort()
    if planes[0] == 0:
        planes.remove(0)
    minimum += planes[0]
    planes[0] -= 1

print(maximum, minimum)
