n = int(input())

for i in range(n):
    word = list(i for i in input())
    length = len(word)
    if length > 10:
        print(word[0] + str(length-2) + word[length - 1])
    else:
        for i in word:
            print(i, end='')
        print('')