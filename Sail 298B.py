t, sx, sy, ex, ey = map(int, input().split())

wind = [i for i in input()]

count = 0
flag = False

for i in wind:
    if i == 'E' and sx < ex:
        sx += 1
    elif i == 'W' and sx > ex:
        sx -= 1
    elif i == 'N' and sy < ey:
        sy += 1
    elif i == 'S' and sy > ey:
        sy -= 1

    count += 1

    if sx == ex and sy == ey:
        flag = True
        break

if flag:
    print(count)
else:
    print('-1')
            
