"""
Largest Sum Contiguous Subarray problem
similar approach to "subsequence of maximal sum"
better known as "Kadane's algorithm"
but more suitable approach to this problem is 
"Max Sum in Contiguous Subarray" or "Largest Sum Contiguous Subarray"
algorithm can be found on GFG
"""

n = int(input())
arr = [int(i) for i in input().split()]
S = 0

for i in range(n):
    if arr[i] == 0:
        arr[i] = 1
    else:
        S += 1
        arr[i] = -1

max_so_far = S-1
max_ending_here = S

for i in range(n):
    max_ending_here = max_ending_here + arr[i]

    if max_ending_here < S:
        max_ending_here = S

    elif max_ending_here > max_so_far:
        max_so_far = max_ending_here

if S != 1:
    print(max_so_far)
else:
    print(0)