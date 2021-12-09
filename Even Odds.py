n, k = map(int, input().split())

# after analysis
odd = (n+1) // 2
even = n // 2

if k <= odd:
    # odd side
    print(int(k*2)-1)
else:
    # even side
    print(int(k-odd)*2)