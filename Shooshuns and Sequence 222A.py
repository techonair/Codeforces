n, k = map(int, input().split())

s = [int(i) for i in input().split()]

dub= s[:]

flag = False
count = 0

if n <= 1:
    flag = True

elif n > 1:
    for i in s:
        if int(i) == s[0]:
            flag = True
        else:
            flag = False

    if flag == False:
        for i in range(n):
            count += 1
            s.append(s[k-1])
            s.pop(0)
            if s != dub:
                first = [s[0]*n]
                
                if s == first:
                    flag = True
                else:
                    flag = False
                    break
            elif s == dub:
                flag = False
                break

            if flag:
                break
            else:
                continue

if flag:
    print(count)
else:
    print(-1)
