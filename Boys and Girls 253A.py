INPUT = open('input.txt', 'r')
OUTPUT = open('output.txt', 'w')

n, m = map(int, INPUT.read().split())

if n > m:
    OUTPUT.write('BG'*m + 'B'*(n-m))
else:
    OUTPUT.write('GB'*n + 'G'*(m-n))