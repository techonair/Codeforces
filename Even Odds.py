n, k = map(int, input().split())

odd = (n+1) // 2
even = n // 2

if k <= odd:
    print(int(k*2)-1)
else:
    print(int(k-odd)*2)