

n = int(input())

new = []
cnt = 0
for i in range(n):
    word = input()

    for i in range(len(word)):
        if i != len(word) - 1:
            if word[i] == word[i+1]:
                pass
            elif word[i] in word[i+1:]:
                break
        else:
            cnt += 1
print(cnt)


# 1 2  2 9    9 22   22 41
# 1    7      13     19

# 6 12 18

# 1 4  13
# 3 9
