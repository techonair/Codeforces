n = int(input())

f = [0,1]

for i in range(2, n):
    var = f[i-2] + f[i-1]
    if var == n or var > n:
        break
    else:
        f.append(var)

len_f = len(f) -1
flag = False

for i in range(len_f, -1, -1):
    for j in range(len_f, -1, -1):
        for k in range(len_f, -1, -1):
            if f[i] + f[j] + f[k] == n:
                x, y, z = f[i], f[j], f[k]
                flag =True
                break

if flag:
    print(x, y, z)
else:
    print("I'm too stupid to solve this problem")


"""
# This prints whole series of possible outcomes
for i in range(len_f, -1, -1):
    print('i', i)
    for j in range(len_f, -1, -1):
        for k in range(len_f, -1, -1):
            if f[i] + f[j] + f[k] == n:
                print(f[i], f[j], f[k])
                break
"""
