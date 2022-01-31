n = int(input())
time = []

for i in range(n):
    time.append(hour+minute)
    hour, minute = input().split()

count_max = 1
count = 1
for i in range(1,n):
    if time[i] == time[i-1]:
        count += 1
    else:
        count = 1

    if count > count_max:
        count_max = count 

print(count_max)