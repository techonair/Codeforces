a,b,c = map(int,input().split())

lis=[0] * 1000001

for i in range(1, 1000001):
    j = i
    while j <= 1000000:
        lis[j] += 1
        j += i
ans = 0    
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            ans += (lis[i*j*k]%(1073741824*2**30))
            
print(ans)      
# submit with pypy that works faster

"""
from cmath import sqrt

a, b, c =  map(int, input().split())

ans =  0

def divisor(i, j, k):
    pro = (((i%(1073741824*2**30)*j%(1073741824*2**30))%(1073741824*2**30))*k%(1073741824*2**30))%(1073741824*2**30)
    count = 0
    for x in range(1, pro+1):
        print(x)
        if pro % x == 0:
            count += 1

    return count

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            ans += divisor(i, j, k)%(1073741824*2**30)

print(ans)
"""