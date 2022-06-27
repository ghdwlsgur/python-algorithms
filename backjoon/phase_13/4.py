
# import sys

# n = int(sys.stdin.readline())
# dic = dict()
# dic['v'] = []
# dic['max'] = 0
# total_index = 0

# for i in range(6):
#     loc, v = map(int, sys.stdin.readline().split())
#     dic['v'].append(v)
#     if dic["max"] <= dic['v'][i]:
#         dic["max"] = dic['v'][i]

# total_area = 1
# for i in range(0, len(dic['v'])):
#     if dic['v'][i] == dic["max"]:
#         total_area *= dic["max"]
#         total_index += i

# print(total_area)
# exclude = 0
# if total_index == 1:
#     exclude = dic['v'][3] * dic['v'][4]
# elif total_index == 3:
#     exclude = dic['v'][4] * dic['v'][5]
# elif total_index == 5:
#     if dic['v'].index(dic['west']) == 0 or dic['v'].index(dic['north']) == 0:
#         exclude = dic['v'][2] * dic['v'][3]
#     else:
#         exclude = dic['v'][0] * dic['v'][5]
# elif total_index == 7:
#     exclude = dic['v'][0] * dic['v'][1]
# elif total_index == 9:
#     exclude = dic['v'][1] * dic['v'][2]


# print((dic['north'] * dic['west'] - exclude) * n)


# import sys
# n = int(sys.stdin.readline())
# arr = []
# max_index_value = [(0, 0), (0, 0)]

# for i in range(6):
#     d, w = map(int, sys.stdin.readline().split())
#     d = 0 if d <= 2 else 1
#     if w > max_index_value[d][1]:
#         max_index_value[d] = (i, w)
#     arr.append((d, w))

# total_area = max_index_value[0][1] * max_index_value[1][1]
# check = [False] * 6

# for idx, _ in max_index_value:
#     for i in [idx, (idx + 1) % 6, idx - 1]:
#         check[i] = True

# exclude_area = 1
# for i in range(6):
#     if not check[i]:
#         exclude_area *= arr[i][1]
# print((total_area-exclude_area)*n)

# import sys
# n = int(sys.stdin.readline())
# arr = []
# max_index_value = [(0, 0), (0, 0)]

# for i in range(6):
#     d, w = map(int, sys.stdin.readline().split())
#     d = 0 if d <= 2 else 1
#     if w > max_index_value[d][1]:
#         max_index_value[d] = (i, w)
#     arr.append((d, w))

# total_area = max_index_value[0][1] * max_index_value[1][1]
# check = [False] * 6

# for idx, _ in max_index_value:
#     for i in [idx, (idx + 1) % 6, idx - 1]:
#         check[i] = True

# exclude_area = 1
# for i in range(6):
#     if not check[i]:
#         exclude_area *= arr[i][1]
# print((total_area - exclude_area) * n)


# import sys
# n = int(sys.stdin.readline())
# arr = []
# max_index_value = [(0, 0), (0, 0)]

# for i in range(6):
#     d, w = map(int, sys.stdin.readline().split())
#     d = 0 if d <= 2 else 1
#     if w > max_index_value[d][1]:
#         max_index_value[d] = (i, w)
#     arr.append((d, w))

# total_area = max_index_value[0][1] * max_index_value[1][1]
# check = [False] * 6

# exclude_area = 1
# for idx, _ in max_index_value:
#     if not check[i]:
#         exclude_area *= arr[i][1]
# print((total_area - exclude_area) * n)

# import sys
# n = int(sys.stdin.readline())
# arr = []
# max_index_value = [(0, 0), (0, 0)]

# for i in range(6):
#     d, w = map(int, sys.stdin.readline().split())
#     d = 0 if d <= 2 else 1
#     if w > max_index_value[d][1]:
#         max_index_value[d] = (i, w)
#     arr.append((d, w))

# total_area = max_index_value[0][1] * max_index_value[1][1]
# check = [False] * 6

# exclude_area = 1
# for idx, _ in max_index_value:
#     if not check[i]:
#         exclude_area *= arr[i][1]
# print((total_area - exclude_area) * n)

import sys 
n = int(sys.stdin.readline())
arr = []
max_index_value = [(0, 0), (0, 0)]

for i in range(6):
    d, w = map(int, sys.stdin.readline().split())
    d = 0 if d <= 2 else 1
    if w > max_index_value[d][1]:
        max_index_value[d] = (i, w)
    arr.append((d, w))

total_area = max_index_value[0][1] * max_index_value[1][1]
check = [False] * 6

exclude_area = 1 
for idx, _ in max_index_value:
  if not check[i]:
    exclude_area *= arr[i][1]
print((total_area - exclude_area) * n)