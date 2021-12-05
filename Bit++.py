n = int(input())

count = 0

for i in range(n):
    command = input()
    if command == '++X' or command == 'X++':
        count += 1
    else:
        count -= 1
        

print(count)