n = int(input())

money = [i for i in input().split()]

twenty5 = 0
fifty = 0
hundred = 0

flag = True

for i in range(n):
    if money[i] == '25':
        twenty5 += 1
    elif money[i] == '50':
        if twenty5 > 0:
            twenty5 -= 1
        else:
            flag = False
            break
        fifty += 1
    elif money[i] == '100':
        if fifty > 0 and twenty5 > 0:
            fifty -= 1
            twenty5 -= 1
        elif fifty == 0  and twenty5 > 1:
            twenty5 -= 2
        elif fifty >= 0 and twenty5 <= 1:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')

"""
# if it was not about the note of 25, 50 and 100 and just if change can be arranged 
# then below code could be submitted
n = int(input())

money = [int(i) for i in input().split()]

stored = 0

flag = True

for i in range(n):
    change = money[i] - 25
    if stored >= 0 and change >= 0:
        stored += 25
        stored = stored - change
        if stored <= 0:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')
"""