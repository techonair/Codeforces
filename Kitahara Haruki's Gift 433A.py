n = int(input())

apples = [int(i) for i in input().split()]

apples.sort()

Kazusa = apples[0]
Setsuna = apples[n-1]

flag = False

if n > 1:
    for i in range(n-2, 0, -1):

        if Kazusa < Setsuna:
            Kazusa += apples[i]

        elif Kazusa == Setsuna:
            Kazusa += apples[i]

        elif Kazusa > Setsuna:
            Setsuna += apples[i]
        
    if Kazusa == Setsuna:
        flag = True
    else:
        flag = False

elif n <= 1:
    flag = False
    
if flag:
    print('YES')
else:
    print('NO')