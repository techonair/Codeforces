n, k = map(int, input().split())

correct = [int(i) for i in input().split()]
wrong = [int(i) for i in input().split()]

min_wrong = min(wrong)

correct.sort()
min_correct = 2 * correct[0]
tl = correct[len(correct)-1]

flag = False

if len(correct)== 1 or (min_correct > tl and min_correct < min_wrong):
    tl = min_correct

if min_correct <= tl and tl < min_wrong:
    print(tl)
else:
    print(-1)