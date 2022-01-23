n = int(input())

upper = []
lower = []

polarity = []

for i in range(n):
    x, y = map(int, input().split())
    upper.append(x)
    lower.append(y)
    # polarity checks if x, y is a combination of even and odd numbers or not.
    if (x % 2 == 0 and y % 2 ==0) or (x % 2 != 0 and y % 2 != 0):
        polarity.append(False)
    else:
        polarity.append(True)

sum_up = sum(upper)
sum_low = sum(lower)

if sum_up % 2 == 0 and sum_low % 2 == 0:
    print(0)
elif sum_up % 2 != 0 and sum_low % 2 != 0:
    if any(polarity):
        print(1)
    else:
        print(-1)
else:
    print(-1)