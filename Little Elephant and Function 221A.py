"""
# My personal comment:
# I submitted out the solution and got a runtime error on 'Test 8 for 1000'
# I was unaware that python has a recursion limit to avoid stack overflow
# The default limit is approximately 10^3. (However I was personally able to go till 998)
# I was able to inrease this limit after reading a GeeksForGeeks article

# https://www.geeksforgeeks.org/python-handling-recursion-limit/

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

"""

import sys
 
sys.setrecursionlimit(10**4)

n = int(input())

a = []
# swap
for i in range(1,n+1):
    a.append(i)

def f(x):
    
    if x == 1:
        return 0
    elif x == 0:
        return 0
    else:
        f(x-1)

    for i in range(len(a)):
        if i > 0:
            s = a[i-1]
            a[i-1] = a[i]
            a[i] = s

f(n)
for i in a:
    print(i, end = ' ')