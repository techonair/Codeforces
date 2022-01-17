n, k = map(int, input().split())

correct = [int(i) for i in input().split()]
wrong = [int(i) for i in input().split()]

correct.sort()

tl = correct[len(correct)-1]
min_corr = correct[0]

min_wrong = min(wrong)

flag = False

if len(correct) > 1 and tl != min_corr:
    if 2 * min_corr <= tl and min_wrong > tl:
        flag = True
elif len(correct) == 1 or tl == min_corr:
    tl = tl * 2
    if 2 * min_corr <= tl and min_wrong > tl:
        flag = True

if flag:
    print(tl)
else:
    print(-1)