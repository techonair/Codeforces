import itertools

happy = []

happy_sum = 0

per = [list(i) for i in itertools.permutations([0, 1, 2 , 3, 4], 5)]

for i in range(5):
    happy.append([int(i) for i in input().split()])

for i in range(len(per)):
    
    temp = (happy[per[i][0]][per[i][1]]+happy[per[i][1]][per[i][0]])*1\
            + (happy[per[i][1]][per[i][2]]+happy[per[i][2]][per[i][1]])*1\
            + (happy[per[i][2]][per[i][3]]+happy[per[i][3]][per[i][2]])*2\
            + (happy[per[i][3]][per[i][4]]+happy[per[i][4]][per[i][3]])*2
    happy_sum = max(happy_sum, temp)

print(happy_sum)