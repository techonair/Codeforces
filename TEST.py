n, k = map(int, input().split())

seq = [int(i) for i in input().split()]

kth = seq[k-1]
flag = False

if n > 1:

    for i in range(k-1, n):
        if seq[i] == kth:
            flag = True
        else:
            flag = False
            break
else:
    flag = True

temp = 0

if flag:
    if n > 1:
        for i in range(k-1, -1, -1):
            if seq[i] == kth:
                temp = i
                continue
            else:
                break
        print(temp)
    else:
        print(temp)
    
else:
    print(-1)