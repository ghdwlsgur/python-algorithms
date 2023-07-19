"""
캐시

이 문제는 '조건'에도 나와있지만 LRU 캐시 교체 알고리즘을 구현하는 문제이고, 이미 잘 알고 있다면 또는 검색해봤다면
잘 구현된 LRU 알고리즘 코드는 많이 찾을 수 있습니다. 단, 이 문제에는 입출력 예제에 캐시 사이즈 0이 포함되어 있습니다.
공개된 대부분의 LRU 구현 코드는 0일 때의 비정상적인 상황은 가정하지 않고 있기 때문에 생각 없이 그냥 가져와 붙인다면
에러가 나서 많이 고생했을 거 같네요. 하지만 사이즈 0을 처리하는 예외 처리 자체는 어렵지 않게 구현할 수 있으므로
입출력 예제가 왜 자꾸 틀리는지를 유심히 살펴봤다면 쉽게 풀 수 있는 문제입니다.
"""

from collections import deque
def solution(cacheSize, cities):
    l = [''] * cacheSize
    cache = deque(l, maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer

testcase = [
	[3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']],
	[3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']]
]

for case in testcase:
    print(solution(case[0], case[1]))

