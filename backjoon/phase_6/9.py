

inp = input()
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in alphabet:
    if i in inp:
        inp = inp.replace(i, "*")
print(len(inp))
