n = int(input())

towns = [int(i) for i in input().split()]

minimum = 10**9
travel = True

for t in range(len(towns)):
    if towns[t] < minimum:
        minimum = towns[t]
        town_num = t+1

    elif towns[t] == min(towns):
        travel = False
        break
    

if travel:
    print(town_num)
else:
    print('Still Rozdil')
