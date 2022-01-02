n = int(input())

s = [int(i) for i in input().split()]

uni = []

ss = s[:]

# only thing left in this solution is to check if a number doesn't have uniform distance
# throughout the array then remove it
# Example: 
# 6
# 1 2 2 1 1 2

# from here 
for i in range(len(ss)):
    count= 0
    for j in range(i, len(ss)):
        if count == 0:
            if s[i] == s[j]:
                count += 1
                d = j-i
        else:
            continue
# to here needs edit

distance = [0 for i in range(n)]

if n > 1:
    for i in range(n):
        if s[i] not in uni:
            uni.append(s[i])
        for j in range(i+1, n):
            if i<len(uni):
                if s[j] == uni[i]:
                    distance[i] = j-i
                    

output=[]
if len(uni) > 0:
    print(len(uni))
    for i in range(len(uni)):
        output.append([uni[i], distance[i]])
    output.sort()
    for i in output:
        print(i[0], i[1])
else:
    print(n)
    print(s[0], distance[0])
