m = input()
n = input()
f = str()

for i in range(len(m)-1 , -1 , -1):
    f += m[i]

print(m)

if f == n:
    print('YES')
else:
    print('NO')