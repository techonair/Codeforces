n = int(input())

for i in range(n*2 + 1):
    space = n - i
    # no space in n/2 or middle most line of whole pattern in vertical, space = n - n = 0
    # after middle most line increasing spaces
    if space < 0:
        space = -space
    s = '  ' * space
    st = ''
    for j in range(n - space):
        st += str(j) + ' '
    s += st + str(n - space) + st[::-1]
    print(s)

"""
for i in range(n, -1, -1):
    print("  "*i, end = "")
    print(" ".join(str(j) for j in range(n-i+1)), " ".join(str(k)for k in range(n-i-1, -1, -1)))

for i in range(1,n+1):
    print("  "*i, end = "")
    print(" ".join(str(j) for j in range(n-i+1)), " ".join(str(k)for k in range(n-i-1, -1, -1)))
"""