s, n = map(int, input().split())

dragon_bonus = []

for i in range(n):
    dragon_bonus.append(list(map(int, input().split())))

dragon_bonus.sort()

flag = False

for i in dragon_bonus:

    if s > i[0]:
        s += i[1]
        flag = True
    else:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
