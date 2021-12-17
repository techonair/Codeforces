n= input()

def ismagicnumber(number):
    if n[0] != '1':
        return False

    for i in range(len(n)):
        if n[i] != '1' and n[i] != '4':
            return False

    for i in range(1, len(n)-1):
        if n[i] == '4' and n[i-1] == '4' and n[i+1] == '4':
            return False
    return True
    
flag = ismagicnumber(n)

if flag:
    print('YES')
else:
    print('NO')
    