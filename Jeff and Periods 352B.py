n = int(input())

s = [int(i) for i in input().split()]

uni = []

if n > 1:
    for i in range(n):
        num = s[i]
        if num not in uni:
            uni.append(num)
            for j in range(i+1, n):
                if j == n-1:
                    print(num, 0)
                    break
                elif s[j] == num:
                    print(num, j-i)
                    break
else:
    print(s[0], 0)
        
        