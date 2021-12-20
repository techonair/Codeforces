n, a, b = input().split()

pos = int(n)-int(a)
sum = int(b)+1
if pos > sum:
    print(sum)
elif pos < sum:
    print(pos)
else:
    print(pos)

"""
count = 0

flag = True


if int(b) != 0:
    for i in range(int(a)+1, int(n)+1):
            count += 1
else:
    flag = False


if flag:
    print(count)
else:
    print(1)
    
"""