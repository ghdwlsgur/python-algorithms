# OX 퀴즈

# def solution(quiz):
#     answer = []
#     for q in quiz:
#         sp = q.split("=")
#         quiz_answer = sp[1]
#         a = sp[0].split()
#         if a[1] == '-':
#             if (int(a[0]) - int(a[2])) == int(quiz_answer):
#                 answer.append("O")
#             else:
#                 answer.append("X")
#         elif a[1] == '+':
#             if (int(a[0]) + int(a[2])) == int(quiz_answer):
#                 answer.append("O")
#             else:
#                 answer.append("X")
#     return answer

def solution(quiz):
    answer = []
    for q in quiz:
        L, R = q.split(' = ')
        a, op, b = L.split()
        if op == '+':
            result = 'O' if int(a) + int(b) == int(R) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a) - int(b) == int(R) else 'X'
            answer.append(result)
    return answer



print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))