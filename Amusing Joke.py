guest = input()
host = input()
joke = input()

names = guest + host

name_letter = dict((n, names.count(n)) for n in set(names))

joke_letter = dict((j, joke.count(j)) for j in set(joke))

if name_letter == joke_letter:
    print('YES')
else:
    print('NO')
    