# 한 번만 등장한 문자

def solution(s):
    answer = []
    for alphabet in list(set(s)):
        if list(s).count(alphabet) == 1:
            answer.append(alphabet)

    return ''.join(sorted(answer))



print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))