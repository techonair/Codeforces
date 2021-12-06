n, k = map(int, input().split())

ls =[]

for i in range(1,n+1):
    if i%2 != 0:
        ls.append(i)

for i in range(1,n+1):
    if i%2 ==0:
        ls.append(i)

print(ls[k-1])