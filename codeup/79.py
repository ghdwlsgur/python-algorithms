

# n = int(input())


# i = 0
# sum = 0
# while i >= 0:
#     i = i+1
#     sum += i
#     if sum == n:
#         break

# print(i)

n = int(input())

sum = 0
for i in range(1, n+1):
    sum += i
    if sum >= n:
        print(i)
        break
