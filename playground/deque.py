from collections import deque

q = deque('abc')

for elm in q:
    print(elm)

q.append('d')
q.appendleft('e')
print(q)

q.pop()
q.popleft()
print(q)

q.extendleft('1234')
print(q)

q.extend('5678')
print(q)

q.clear()
print(q)