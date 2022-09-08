# 에디터

# ! 시간초과
# import sys

# global cursor

# text = sys.stdin.readline().rstrip()
# cursor = len(text)
# listBuff = list(text)

# for _ in range(int(sys.stdin.readline().rstrip())):
#     input = sys.stdin.readline().split()

#     if input[0] == "P":
#         listBuff[:int(cursor)] += input[1]
#         cursor += 1
#     if input[0] == "L":
#         if cursor > 0:
#             cursor -= 1
#     if input[0] == "D":
#         if cursor <= len(listBuff):
#             cursor += 1
#     if input[0] == "B":
#         if cursor > 0:
#             cursor -= 1
#             listBuff.pop(cursor)
# print("".join(listBuff))

# ! 데크
# import sys
# from collections import deque

# textBuffOrigin = list(sys.stdin.readline().rstrip())
# textBuffBucket = deque()

# for _ in range(int(sys.stdin.readline().rstrip())):
#     input = sys.stdin.readline().split()
#     if input[0] == "L":
#         if textBuffOrigin:
#             textBuffBucket.appendleft(textBuffOrigin.pop())
#     elif input[0] == "D":
#         if textBuffBucket:
#             textBuffOrigin.append(textBuffBucket.pop())
#     elif input[0] == "B":
#         if textBuffOrigin:
#             textBuffOrigin.pop()
#     elif input[0] == "P":
#         textBuffOrigin.append(input[1])

# textBuffOrigin += textBuffBucket
# print("".join(textBuffOrigin))


import sys

textBuffOrigin = list(sys.stdin.readline().rstrip())
textBuffBucket = []

for _ in range(int(sys.stdin.readline().rstrip())):
    input = sys.stdin.readline().split()
    if input[0] == "L":
        if textBuffOrigin:
            textBuffBucket.append(textBuffOrigin.pop())
    elif input[0] == "D":
        if textBuffBucket:
            textBuffOrigin.append(textBuffBucket.pop())
    elif input[0] == "B":
        if textBuffOrigin:
            textBuffOrigin.pop()
    elif input[0] == "P":
        textBuffOrigin.append(input[1])

textBuffOrigin += reversed(textBuffBucket)
print("".join(textBuffOrigin))
