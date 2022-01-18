n = int(input())

arr = [int(i) for i in input().split()]

sum = 0
for i in range(n):
    sum += arr[i]

"""
Logic: If sum % n == 0: the sum can be redistributed between all the elements, ans = n

       Else I can always keep one element permanently as i keep reducing it to the endless
       and keep other elements increase to some value where n-1 elements get equal
       hence, ans = n-1
"""

if sum % n == 0:
    print(n)
else:
    print(n-1)