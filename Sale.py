n, m = input().split()

prices = list(int(i) for i in input().split())

prices.sort()

sum = 0


for i in range(int(n)):
    if int(m)>0:
        if prices[i]<0:
            sum += -(prices[i])
    else:
        break
    m = int(m) - 1

print(sum)
