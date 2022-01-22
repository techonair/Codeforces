INPUT = open('input.txt', 'r')
OUTPUT = open('output.txt', 'w')

n = int(INPUT.readline())

arr = [int(i)for i in INPUT.readline().split()]

s = [[] for _ in range(5000)]

for i in range(2*n):
    s[arr[i]].append(i+1)

flag = False

for lists in s:
    if lists != [] and len(lists) % 2 == 0:
        for i in range(0, len(lists)-1):
            flag = True
            OUTPUT.write(str(lists[i])+' '+str(lists[i+1])+'\n')
            break

if not flag:
    OUTPUT.write('-1')
print(s)