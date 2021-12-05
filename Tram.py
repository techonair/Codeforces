n = int(input())

a = []
b = []

for i in range(n):
    A, B = input().strip().split()
    a.append(int(A))
    b.append(int(B))

num_passengers = []

for i in range(n):
    if i == 0:
        num_passengers.append(b[i])
    else:
        num_passengers.append(num_passengers[i-1] - a[i] + b[i])

capacity = 0

for passengers in num_passengers:
    if passengers > capacity:
        capacity = passengers

print(capacity)

