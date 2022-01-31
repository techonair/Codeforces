"""
Observation:

Formula : f[n] = f[n-1] - f[n-2]

f1 = 2
f2 = 3
f3 = 1
f4 =-2
f5 =-3
f6 =-1

Values repeat after every six iterations

f7 = 2
f8 = 3
f9 = 1
f10=-2
f11=-3
f12=-1

f13= 2
f14= 3 ....

Pattern => [x, y, y-x, -x, -y, x-y]

To detect at which iteration we are we can use MOD
"""

x, y = map(int, input().split())
n = int(input())

f = [x, y, y-x, -x, -y, x-y]

print(f[(n-1) % 6] % 1000000007)