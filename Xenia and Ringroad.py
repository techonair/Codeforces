n, m = input().split()

homes = [int(i) for i in input().split()]

initial = 1
time = 0

for home in homes:
    time += (home - initial + int(n)) % int(n)
    initial = home

print(time)