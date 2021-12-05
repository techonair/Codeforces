n = int(input())

scores = [int(score) for score in input().split()]

max = 0
min = 0

amazing = 0

for i in range(n):

    if i == 0:
        max = scores[i]
        min = scores[i]
    elif scores[i] > max:
        max = scores[i]
        amazing += 1
    elif scores[i] < min:
        min = scores[i]
        amazing += 1

print(amazing)

