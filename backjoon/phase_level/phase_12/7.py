# import sys
# input = sys.stdin.readline().rstrip()
# s = set()
# str = ""
# k = 1
# loop = False
# while k <= 5:
#     for i in range(0, len(input)):
#         if loop:
#             continue
#         for j in range(i + k, (i + k) + 1):
#             str = input[i:j]
#             s.add(str)
#             if j == 5:
#                 loop = True
#         str = ""
#     loop = False
#     k += 1
# print(len(sorted(list(s))))


import sys
input = sys.stdin.readline().rstrip()

cnt = 0 
for i in range(len(input)):
    s = set()
    for j in range(len(input)-i):             
        s.add(input[j:j+i+1])    
    cnt += len(s)
print(cnt)