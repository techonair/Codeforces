"""
We count the total_ones in the array and total_zeros
We will note the first_occurence of zero and last_occurence
In between first_occurence and last occurence count number of ones (bt_ones)
ans = last_occurence - first_occurence + total_ones - bt_ones + 1
if total_ones != len(arr):
    print(ans)
elif total_zeros != 0:
    print(total+1)
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