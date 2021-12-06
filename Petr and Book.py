n = int(input())

pages = list(int(i) for i in input().split())

sum = 0

while True:
    if sum<n:
        for p in range(len(pages)):
            sum += pages[p]
            if sum>=n:
                day = p + 1
                break
            else:
                day = p + 1
    elif sum>=n:
        break

print(day)