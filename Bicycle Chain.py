n = int(input())

front = list(int(i) for i in input().split())

m = int(input())

rear = list(int(i) for i in input().split())

gear  = []

max = 0
max_ratio = 0

for i in rear:
    for j in front:
        ratio = i/j
        # print(i/j, ratio.is_integer())
        if ratio.is_integer():
            gear.append(i/j)


for i in gear:
    
    if i >= max_ratio:
        if i != max_ratio:
            max_ratio = i
            max = 1
        
        elif i == max_ratio:
            max_ratio = i
            max += 1
            

print(max)
