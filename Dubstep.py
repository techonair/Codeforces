"""
s = input()
ls = len(s)
#print('len', ls)

song =''
start = 0
end = ls -1

for i in range(0, ls, 3):
    if s[i:i+3] == 'WUB':
        start = i+3
    else:
        break

for i in range(ls-1, -1, -3):
    if s[i-2 : i+1] == 'WUB':
        end = i-2
    else:
        break

#print(start, end)

i = start
while i <= end:
    if s[i]=='W' and s[i+1]=='U' and s[i+2]=='B': #this -> 'i<end' <- is feature + bug
        i += 3
        song += ' '  
    else:
        song += s[i]
        i += 1

print(song)
"""

n = [i for i in input().split('WUB') if i != '']

for i in n:
    print(i, end=' ')