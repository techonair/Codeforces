n, m =  map(int, input().split())

planes = []

for i in range(m):
    p = int(input())
    planes.append(p)

max=0
while n>=1:
    for i in range(len(planes)):
        if planes[i] != 0:
            planes - i