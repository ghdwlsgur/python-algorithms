"""
비밀 지도
이 문제는 비트 연산(Bitwise Operation)을 묻는 문제입니다. 이미 문제 예시에 2진수로 처리하는 힌트가 포함되어 있고,
둘 중 하나가 1일 경우에 벽 #이 생기기 때문에 OR로 처리하면 간단히 풀 수 있습니다. 아주 쉬운 문제였던 만큼 if else
로 풀이한 분들도 많이 발견되었는데요. 정답으로는 간주되지만 이 문제는 비트 연산을 잘 다룰 수 있는지를 묻고자 하는 의도
였던 만큼 앞으로 이런 유형의 문제를 풀 때는 비트 연산을 꼭 기억하시기 바랍니다.
"""

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        answer.append(bin(i | j)[2:].zfill(n).replace('1', '#').replace('0', ' '))
    return answer


testcase = [(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]),
            (5, [9, 3, 28, 18, 11], [30, 1, 21, 17, 28]),
            (6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])]

for i, j, k in testcase:
    print(solution(i, j, k))