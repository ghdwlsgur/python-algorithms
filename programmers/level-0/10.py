# 최빈값 구하기

# 다른 사람 풀이
def solution2(array):
    while len(array) != 0:
        # 세트 자료향으로 배열에 존재하는 유니크 숫자 추출
        for i, a in enumerate(set(array)):
            # 유니크 숫자를 현재 배열에서 제거
            array.remove(a)
        # 모든 원소를 제거하였으므로 최종적으로 남는 숫자가 최빈값을 의미
        # 파이썬에서는 'for'루프가 끝나더라도 마지막에 사용된 루프 변수를 유지한다.
        # 루프 변수가 함수나 클래스 같은 블록 안에 있지 않다면 전역 스코프에서
        # 사용되므로 루프가 끝난 후에도 변수를 사용 가능
        if i == 0:
            return a
    # i가 0이 아니라는 것은 최빈값이 여러 개 존재, 따라서 -1 반환
    return -1


# 나의 풀이
def solution(array):
    l = []
    max_cnt = 0
    answer = []
    for num in list(set(array)):
        cnt = array.count(num)
        if cnt > max_cnt:
            max_cnt = cnt
            answer.append(num)
        l.append(cnt)
    if l.count(max(l)) >= 2:
        return -1
    return answer[-1]



# print(solution([1, 2, 3, 3, 3, 4]))
# print(solution([1, 1, 2, 2]))
# print(solution([1]))
# print(solution([0, 0, 1]))

print(solution2([1, 2, 3, 3, 3, 4]))
print(solution2([1, 1, 2, 2]))
print(solution2([1]))
print(solution2([0, 0, 1]))