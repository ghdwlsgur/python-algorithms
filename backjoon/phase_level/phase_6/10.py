

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
