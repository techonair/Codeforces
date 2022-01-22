from math import sqrt
 
n = int(input())

ans = 0
for a in range(1, n+1):
    for b in range(a, n+1):
        c = int(sqrt(a*a + b*b))
        
        if c <= n and c*c == a*a + b*b:
            ans+=1
print(ans)

# submit with pypy