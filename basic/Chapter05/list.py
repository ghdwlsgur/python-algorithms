s = "show how to index into sequences".split()


print(s[1:4])
print(s[1:-1])
print(s[3:])
print(s[:3])

full_slice = s[:]
print(full_slice)
print(full_slice == s)
print(full_slice is s)

u = s.copy()
v = list(s)

print(u)
print(v)
print(s[::-1])
