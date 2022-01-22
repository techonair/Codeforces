INPUT = open('input.txt', 'r')
OUTPUT = open('output.txt', 'w')

n = int(INPUT.readline())

arr = [int(i)for i in INPUT.readline().split()]

s = [[] for _ in range(5001)]

for i in range(2*n):
    s[arr[i]].append(i+1)

if any(len(lists) % 2 != 0 for lists in s):
    OUTPUT.write('-1')

else:
    for lists in s:
        if lists != [] and len(lists) % 2 == 0:
            i = 0
            flag = True
            while i < len(lists) - 1:
                OUTPUT.write(str(lists[i])+' '+str(lists[i+1])+'\n')
                i+=2