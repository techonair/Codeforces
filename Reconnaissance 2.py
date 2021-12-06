n = int(input())

soldiers = list(int(i) for i in input().split())

rec_1 = 0
rec_2 = 0
min = 1000

for s in range(len(soldiers)):

    z = s+1
    if z< len(soldiers):
        diff = soldiers[s] - soldiers[z]
        if diff <= min and diff >= 0:
            rec_1 = s+1
            rec_2 = z+1
            min = diff

print(rec_1, rec_2)