
# 나의 풀이
# 시간 입력 받기
# hour = int(input())
#
# cnt = 0
#
# # 0 ~ 입력 받은 시간
# for hh in range(hour+1):
#     # 0 ~ 59분
#     for mm in range(60):
#         # 0 ~ 59초
#         for ss in range(60):
#             # 문자열 변환
#             time = str(hh)+str(mm)+str(ss)
#             # 3이 포함될 경우 카운트
#             if "3" in time:
#                 cnt += 1
# print(cnt)

# 동빈나 풀이
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
