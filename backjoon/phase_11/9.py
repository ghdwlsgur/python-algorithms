
# ! case 1 (시간 초과)
# import sys
# n = int(sys.stdin.readline())
# l = []
# for i in range(n):
#     input = list(map(str, sys.stdin.readline().split()))
#     input.append(i)
#     l.append(input)

# l.sort()
# for i in range(0, len(l)):
#     for j in range(i+1, len(l)):
#         temp = []
#         if l[i][0] == l[j][0] and l[i][2] > l[j][2]:
#             temp = l[i]
#             l[i] = l[j]
#             l[j] = temp
#     temp = []
# for a, b, _ in l:
#     print(a, b)

# import sys
# n = int(sys.stdin.readline())
# l1 = []
# for i in range(n):
#     input = list(map(str, sys.stdin.readline().split()))
#     input[0] = int(input[0])
#     input.append(i)
#     l1.append(input)

# l1.sort(key=lambda x: [x[0], x[2]])
# for a, b, _ in l1:
#     print(a, b)
