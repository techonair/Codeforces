n = int(input())

soldiers = list(int(i) for i in input().split())
arr= []

big = max(soldiers)

for i in range(n):
    if soldiers[i] == big:
        arr.append(i)

big_in = min(arr)
    
arr.clear()

small = min(soldiers)

for i in range(n):
    if soldiers[i] == small:
        arr.append(i)

small_in = max(arr)

#print(big_in, small_in)

if big_in > small_in:
    swaps = (big_in-1 + n-small_in) -1
else:
    swaps = big_in-1 + n-small_in

print(swaps)
