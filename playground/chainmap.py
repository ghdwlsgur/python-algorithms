from collections import ChainMap

a = {'a': 'A', 'c': 'C1'}
b = {'b': 'B', 'c': 'C2'}

m = ChainMap(a, b)

print(list(m.keys()))
print(list(m.values()))