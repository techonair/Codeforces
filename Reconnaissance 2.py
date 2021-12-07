n = int(input())

soldiers = list(int(i) for i in input().split())

# the difference of first and last 
diff = abs(soldiers[0]- soldiers[n-1])
rec_1 = n # last element 
rec_2 = 1 # first element

m = 1001
minimum = min(m, diff)

for s in range(len(soldiers)-1):
    diff = abs(soldiers[s] - soldiers[s+1])
    
    if diff<= minimum:
        minimum = diff
        rec_1 = s+2
        rec_2 = s+1

print(rec_1, rec_2)