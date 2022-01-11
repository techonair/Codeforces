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