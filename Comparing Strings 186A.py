a = input()
b = input()
x = sorted(a)
y = sorted(b)

flag = False

count = 0

if x == y:
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            if count <= 2:
                flag = True
            else:
                flag = False
                break

if flag:
    print('YES')
else:
    print('NO')

"""
a_count = {}
b_count = {}

if len(a) == len(b):
    for i in range(len(a)):
        if a[i] not in a_count:
            a_count[a[i]] = 1
        else:
            a_count[a[i]] += 1
        
    for j in range(len(b)):
        if b[j] not in b_count:
            b_count[b[j]] = 1
        else:
            b_count[b[j]] += 1

    if a_count == b_count:
        flag = True

print(a_count)
print(b_count)

if flag:
    print('YES')
else:
    print('NO')
    
"""