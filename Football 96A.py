n = input()

danger_1 = '0000000'
danger_2 = '1111111'

flag = False

#print('len:', len(n))

for i in range(len(n)-6):
    #print(i)
    if n[i] == '1' and n[i:i+7] == '1111111':
        flag = True
        break
    elif n[i] == '0' and n[i:i+7] == '0000000':
        flag = True
        break

if flag:
    print('YES')
else:
    print('NO')