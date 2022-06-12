words = input()


res = []

if len(words) == 1:
    print(words.capitalize())
else:
    for i in range(0, 26):
        res.append(0)
    for alpha in words:
        res[ord(alpha.capitalize()) - 65] += 1

    if res.count(max(res)) > 1:
        print("?")
    else:
        print(chr(int(res.index(max(res))) + 65))
