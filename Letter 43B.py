head = [i for i in input() if i!= ' ']

string = [i for i in input() if i!= ' ']

for i in string:
    if i in head:
        flag = True
        head.remove(i)
    else:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')