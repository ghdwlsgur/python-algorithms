import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())


dic = dict()
for i in l:
    if dic.get(i):
        dic[i] += 1
    else:
        dic[i] = 1


answer = list(map(int, sys.stdin.readline().split()))
for i in answer:
    if dic.get(i):
        print(dic.get(i), end=" ")
    else:
        print(0, end=" ")
