n = int(input())

left = []
right = []

l_count_0 = 0
l_count_1 = 0

r_count_0 = 0
r_count_1 = 0

for i in range(n):
    l, r = input().strip().split()
    left.append(l)
    right.append(r)

    if l == '1':
        l_count_1 += 1
    else:
        l_count_0 += 1
    
    if r == '1':
        r_count_1 += 1
    else:
        r_count_0 += 1

if l_count_0 > l_count_1:
    left_time = len(left)-l_count_0
else:
    left_time = len(left)-l_count_1

if r_count_0 > r_count_1:
    right_time = len(left)-r_count_0
else:
    right_time = len(left)-r_count_1

print(left_time + right_time)


# Below code is for 1 level up problem, here the final state of the doors should not be the same
# that is if left doors are open then right ones must be closed or vice-versa
'''
n = int(input())

left = []
right = []

l_count_1 = 0
r_count_1 = 0

for i in range(n):
    l, r = input().strip().split()
    left.append(l)
    right.append(r)

    if l == '1':
        l_count_1 += 1
    
    if r == '1':
        r_count_1 += 1


if l_count_1 < r_count_1 :
    print(l_count_1 + len(right) - r_count_1)
else:
    print(len(left) - l_count_1 + r_count_1)

'''