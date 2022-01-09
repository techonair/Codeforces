n = int(input())

s = [int(i) for i in input().split()]

num_diff = {}

for i in range(n):
    num = s[i]
    if num not in num_diff:
        num_diff[num] = (i, 0)
    elif num_diff[num][1] >= 0:
        old_diff = num_diff[num][1]
        new_diff = i - num_diff[num][0]
        num_diff[num] = (i, -1 if old_diff and new_diff != old_diff else new_diff)

legal_values = [(i, num_diff[i][1]) for i in sorted(num_diff.keys()) if num_diff[i][1] >= 0]

print(len(legal_values))

for values in legal_values:
    print(values[0], values[1])


