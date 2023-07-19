"""
다트 게임

문자열 처리(String Manipulation)를 묻는 문제입니다. 앞에서부터 한 글자씩 잘라서 처리할 수 있고, 또는 간단한
컴파일러를 만들듯이 토큰화(Tokenizing)와 의미 분석(Semantic Analysis)을 통해 어렵지 않게 계산할 수 있습니다.

점수 중에는 한 자리뿐만 아니라 두 자리인 10점도 포함되어 있기 때문에 한 글자씩 잘라서 처리할 때는 그 부분에 유의해야
합니다. 토큰화로 처리할 때는 정규식을 사용하면 비교적 쉽게 잘라낼 수 있습니다. S,D,T는 각각 원점수, 제곱, 세제곱으로
처리하고 스타상은 두 배로 계산하면 됩니다. 참, 아차상은 마이너스 점수라는 점에 유의하세요.
"""

# def solution(dartResult):
#     answer = []
#     for i, v in enumerate(dartResult, 1):
#         if v == 'S':
#             answer[-1] **= 1
#             pass
#         elif v == 'D':
#             answer[-1] **= 2
#             pass
#         elif v == 'T':
#             answer[-1] **= 3
#             pass
#         elif v == '*':
#             answer[-1] *= 2
#             if len(answer) >= 2:
#                 answer[-2] *= 2
#             pass
#         elif v == '#':
#             answer[-1] *= -1
#             pass
#         else:
#             if dartResult[i-1:i+1] == '10':
#                 answer.append(10)
#             elif dartResult[i-2:i] != '10':
#                 answer.append(int(v))
#
#     return sum(answer)


import re
def solution(dartResult):
    pattern = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
    answer = []
    count = {
        'S': lambda v: v,
        'D': lambda v: v**2,
        'T': lambda v: v**3
    }
    for a, b, c in pattern.findall(dartResult):
        if b == 'S':
            score = count['S'](int(a))
        elif b == 'D':
            score = count['D'](int(a))
        elif b == 'T':
            score = count['T'](int(a))

        if c == '*':
            score *= 2
            if answer:
                answer[-1] *= 2
        elif c == '#':
            score *= -1
        answer.append(score)

    return sum(answer)

print(solution('1S2D*3T'))