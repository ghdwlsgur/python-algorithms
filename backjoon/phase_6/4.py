

for i in range(int(input())):
    a = input().split()
    for alpha in a.pop():
        print(alpha * int(a[0]), end="")
    print()
