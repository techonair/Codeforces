bit = input()

n = len(bit)

for i in range(n):
    if bit[i] == '0':
        bit = bit[0:i] + bit[i + 1:]
        break
if len(bit) == n:
    bit = bit[1:]
print(bit)

"""
bit = [int(i) for i in input()] 

n = len(bit)

for i in bit:
    if i == 0:
        flag = True
        break
    else:
        flag = False
        
if flag:
    bit.remove(0)
    for i in bit:
        print(i, end='')

else:
    bit.remove(bit[0])
    for i in bit:
        print(i, end='')
"""
            
