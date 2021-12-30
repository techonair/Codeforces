t, sx, sy, ex, ey = map(int, input().split())

wind = [i for i in input()]

count = 0

for i in wind:
    
    if ex > sx and ey > sy:
        if i == 'E':
            sx += 1
        elif i == 'N':
            sy += 1
        count += 1

    elif ex > sx and ey < sy:
        if i == 'E':
            sx += 1
        elif i == 'S':
            sy -= 1
        count += 1

    elif ex < sx and ey < sy:
        if i == 'S':
            sy -= 1
        elif i == 'W':
            sx -= 1
        count += 1

    elif ex < sx and ey > sy:
        if i == 'W':
            sx -= 1
        elif i == 'N':
            sy += 1
        count += 1
    
    if sx == ex and sy == ey:
        print(count)
        flag = True
        break
    else:
        flag = False



if not flag:
    print(-1)
