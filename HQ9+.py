prog = ['H', 'Q', '9']

code = list(i for i in input())

run = False

for i in code:
    if i in prog:
        run = True
        break

if run:
    print('YES')
else:
    print('NO')