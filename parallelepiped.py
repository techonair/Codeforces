import math

s1, s2, s3 = input().split()

a = math.sqrt(int(s1) * int(s3) / int(s2))
b = math.sqrt(int(s1) * int(s2) / int(s3))
c = math.sqrt(int(s3) * int(s2) / int(s1))

print(int(4*(a+b+c)))