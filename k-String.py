k = int(input())

string = [i for i in input()]

elements = set(string)

flag = False
output = ''

for i in elements:
    if string.count(i) % k != 0:
        flag = False
        break
    else:
        flag = True
        output += i*(int(string.count(i)/k))

if flag:
    while k > 0:
        print(output, end = '')
        k -= 1

else:
    print(-1)
