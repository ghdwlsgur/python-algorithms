# x 사이의 개수
def solution(myString):
    answer = []
    for word in myString.split('x'):
        answer.append(len(word))
    return answer




print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))