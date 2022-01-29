"""
we can find the indexes of 1s
(the maximum difference between two adjustend indexes +1) = ans
"""

n = int(input())
arr = [int(i) for i in input().split()]
ones = []
maximum_diff = 0

for i in range(n):
    if arr[i] == 1:
        ones.append(i)
    
for i in range(len(ones)):
        maximum_diff = max(maximum_diff, ones[i]-ones[i-1])


if len(ones) == len(arr):
    print(0)
elif maximum_diff == 1 or maximum_diff == 0:
    print(len(arr))
else:
    print(maximum_diff+1)