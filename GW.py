import itertools

resultado = itertools.permutations('abcdef', 3)

for i in resultado:
    print(''.join(i))