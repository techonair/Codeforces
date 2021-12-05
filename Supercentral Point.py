n = int(input())

coordinates = []

for i in range(n):
    coordinates.append(list(int(j) for j in input().split()))

count = 0

for c in coordinates:
    
    right_neighbor = False
    left_neighbor = False
    upper_neighbor = False
    lower_neighbor = False

    for d in coordinates:

        if c != d:
            # neighbor
            if c[0] > d[0] and c[1] == d[1]:
                right_neighbor = True
            elif c[0] < d[0] and c[1] == d[1]:
                left_neighbor = True
            elif c[0] == d[0] and c[1] > d[1]:
                upper_neighbor = True
            elif c[0] == d[0] and c[1] < d[1]:
                lower_neighbor = True

            if right_neighbor and left_neighbor and upper_neighbor and lower_neighbor:

                count += 1

                right_neighbor = False
                left_neighbor = False
                upper_neighbor = False
                lower_neighbor = False
                break

print(count)
