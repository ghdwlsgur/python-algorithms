from collections import defaultdict
s = [('한식', '떡볶이'), ('한식', '불고기'), ('한식', '닭갈비'), ('양식', '행버거'), ('양식', '파스타')]

d = defaultdict(list)

for k, v in s:
    d[k].append(v)

sorted(d.items())

print(d['양식'])
print(d['한식'])