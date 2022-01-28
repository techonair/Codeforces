"""
To find sum of Vi we can do precomputation, suppose we are given l = 3 and r = 5
meaing we need to find sum from index 2 to 4
answer will be, ans = prefix[4] - prefix[1] or prefix[r-1] - prefix[l-2] (if l!= 1)
if l == 1:
    print(prefix[r-1])
Time Complexity = O(N)
""" 

"""
To find sum of Ui we can copy given array and sort it and generate it's prefix array.
And return the rth element - lth element sum just like we did above.
Time Complexity = O(NlogN)

Total time complexity: O(NlogN + N + q)
"""

n = int(input())
prefix = [int(i) for i in input().split()]
q = int(input())
Type = []
l = []
r = []

array = sorted(prefix[:])

for i in range(q):
    x, y, z = input().split()
    Type.append(int(x))
    l.append(int(y))
    r.append(int(z))

for i in range(1, n):
    prefix[i] += prefix[i-1]
    array[i] += array[i-1]
    
for i in range(q):
    if Type[i] == 1:
        if l[i] != 1:
            print(prefix[r[i]-1] - prefix[l[i]-2])
        else:
            print(prefix[r[i]-1])
    else:
        if l[i] != 1:
            print(array[r[i]-1] - array[l[i]-2])
        else:
            print(array[r[i]-1])
