var = ['h', 'e', 'l', 'o']

vasya = input()

ans = 'YES'
# Hello elements in vasya or not
for i in var:
    if i not in vasya:
        ans = 'NO'
        break

l_count = 0

for i in vasya:
    if i=='l':
        l_count += 1

if ans == 'YES':
    H = vasya.index('h')
    E = vasya.index('e')
    L = vasya.index('l')

    if l_count > 1:
        L2 = vasya.index('l', L+1, len(vasya))

    O = vasya.index('o')
    

print(H, E, L, L2, O)

if H < E and E < L and L < L2 and L2 < O:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)

    