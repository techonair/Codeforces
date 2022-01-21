a,b,c = map(int,input().split())

lis=[0]*(1000001)

for i in range(1,1000001):
    j=i
    while j<=1000000:
        lis[j]+=1
        j+=i
ans=0    
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            ans+=(lis[i*j*k]%1073741824)
print(ans)            
 