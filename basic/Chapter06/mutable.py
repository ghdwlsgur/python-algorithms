"""
(mutable)list - mutable한 순서가 있는 객체 집합
(mutable)set - mutable한 순서가 없는 고유한 객체 집합
(mutable)dict - key와 value가 맵핑된 객체, 순서 없음
(immutable)bool - 참, 거짓
(immutable)int - 정수
(immutable)float - 실수
(immutable)tuple - immutable한 순서가 있는 객체 집합
(immutable)str - 문자열
(immutable)frozenset - immutable한 set
"""


from pprint import pprint as pp
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
for key, val in a.items():
    print("key={key}, value={value}".format(key=key, value=val))

print(a)
pp(a)
