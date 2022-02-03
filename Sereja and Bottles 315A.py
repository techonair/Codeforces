# bottle if brand a bottle is '1' then we cannot open another bottle with '1'
# but we can open '2', '3' etc.

n = int(input())

a = [0]*n
b = [0]*n
sum = 0
for i in range(n):
    a[i], b[i] = map(int, input().split())

for i in range(n):
    for j in range(n):
        if i != j and a[i] == b[j]:
            break
    if i != j and a[i] == b[j]:
            continue
    else:
        sum += 1

print(sum)
            
