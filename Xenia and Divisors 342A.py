n = int(input())
 
num = [int(i) for i in input().split()]
 
divs = [0]*8
 
flag = True
 
for i in num:
    divs[i] += 1
 
if divs[5] > 0 or divs[7] > 0 or divs[1]*3 < n:
    flag = False
 
else:
    if divs[2]-divs[4] < 0 or (divs[4] + divs[2]-divs[4] + divs[3]) != divs[1] or (divs[2]-divs[4] + divs[3]) != divs[6]:
        flag = False
        
    
if flag:
    for i in range(divs[4]):
        print("1 2 4")
    for j in range(divs[2]-divs[4]):
        print("1 2 6")
    for k in range(divs[3]):
        print("1 3 6")
 
else:
    print(-1)
    

"""
n = int(input())

num = [int(i) for i in input().split()]

num.sort()

flag = False

ans = set()

for i in range(n):
    for j in range(i, n):
        if num[i] != num[j]:
            for k in range(j, n):
                if num[j] != num[k]:
                    if num[j] % num[i] == 0  and num[k] % num[j] == 0 and num[k] % num[i] == 0:
                        ans.add((num[i], num[j], num[k]))
                        flag = True

if flag:
    for i in sorted(ans):
        print(*i)
            
else:
    print(-1)
    
"""