num = input()
lucky = 0
 
for i in num:
    if i == '4' or i == '7':
        lucky += 1 
 
counter = 0

for c in str(lucky):
    if c == '4' or c == '7':
        counter += 1

if counter == len(str(lucky)):
    print("YES")

else:
    print("NO")

            



