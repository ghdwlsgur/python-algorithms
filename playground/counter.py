from collections import Counter

cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(cnt)
print(cnt['blue'])

c1 = Counter('gallahad')
c2 = Counter({'red': 4, 'blue': 2})
c3 = Counter(cats=4, dogs=8)

print(c1)
print(c2)
print(c3)

del cnt['red']
print(cnt)