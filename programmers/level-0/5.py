# 배열의 원소 삭제하기
def solution(arr, delete_list):
    answer = []
    for i in arr:
       if i not in delete_list:
           answer.append(i)

    return answer


arr = [293, 1000, 395, 678, 94]
delete_list = [94, 777, 104, 1000, 1, 12]

print(solution(arr, delete_list))