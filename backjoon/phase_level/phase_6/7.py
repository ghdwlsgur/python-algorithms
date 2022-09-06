a, b = input().split()


a_ = ""
b_ = ""

for i in range(2, -1, -1):
    a_ += a[i]
    b_ += b[i]


if int(a_) > int(b_):
    print(int(a_))
else:
    print(int(b_))
