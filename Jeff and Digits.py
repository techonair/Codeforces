n = int(input())

num = [i for i in input().split() if i == '5']

real_num_1 = ('5' * len(num)) + ('0' * (n - len(num)))
real_num_2 = ('5' * (len(num) - 1)) + ('0' * (n - (len(num)))) + ('5' * (1))

dummy = [int(real_num_1), int(real_num_2)]

print(dummy)

cummy = []

flag = False

for i in dummy:
    if i % 90 == 0:
        flag = True
        cummy.append(i)
        
    elif int(real_num_2) % 90 == 0:
        flag = True
        cummy.append(i)

if flag:
    print(max(cummy))
else:
    print(-1)

print(dummy[1] % 90)