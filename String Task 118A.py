vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y','y']

s = [i.lower() for i in input() if i not in vowels]

print('.', end='')
print('.'.join(s))