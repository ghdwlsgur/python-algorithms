import sys
def binary_search(arr, target, start, end):
    if start > end:
        return "no"

    mid = (start + end) // 2
    if arr[mid] == target:
        return "yes"
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


n = int(input())
stock_list = list(map(int, input().split()))

m = int(input())
order_list = list(map(int, input().split()))

result = []
for i in order_list:
    result.append(binary_search(stock_list, i, 0, len(stock_list) - 1))


for i in result:
    print(i, end=' ')