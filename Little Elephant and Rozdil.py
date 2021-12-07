n = int(input())

towns = [int(i) for i in input().split()]

dist = towns.sort()
print(dist)

if dist[0] == dist[1]:
    print('Still Rozdil')
else:
    print(towns.index(dist[0]))

"""
minimum = 10**9
travel = True

for t in range(len(towns)):
    if towns[t] == min(towns):
        travel = False
        break
    elif towns[t] < minimum:
        minimum = towns[t]
        town_num = t+1

if travel:
    print(town_num)
else:
    print('Still Rozdil')
     """