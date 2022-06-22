# key - value 형식의 데이터는 어딜 가든 중요하게 여긴다.
# 자바의 hashmap이나 js의 객체나 json 등등

# 파이썬은 딕셔너리(dictionary)라고 한다.
# 선언은 간단하다.
dic = {'hello': 3, 'asdf': 4, 123: 123}
# 데이터 타입은 유연하게 가져갈 수 있으며, 키는 중복되면 안된다.
# 중괄호로 감싸고 k:v, k:v, ... 형식으로 나열

# 인덱싱처럼 하면 값을 리턴 받을 수 있다.
temp = dic['hello']
print(temp)
print(dic[123])

# key 또는 value가 존재하지 않으면 KeyError가 발생한다.
# .get()를 이용해 KeyError를 피할 수 있다.
print(dic.get('not_key'))
# 키가 없으면 None을 반환한다.

# 해당 key가 딕셔너리에 있는지 알고 싶으면
print('hello' in dic)

# key-value 쌍 삭제하는 건 리스트 때 썼던 del 키워드
del dic[123]
print(dic)

# 추가하는 건
dic['new'] = 1234
print(dic['new'])

print(dic)
# 딕셔너리에서 key의 이름을 바꿔야 할 경우, 대입 따로 del 따로 하지 말고 pop()을 사용하자
dic['changed'] = dic.pop('new')
print(dic)

# pop 메소드는 해당 key를 지우는 동시에 value를 리턴한다.
# pop 메소드도 KeyError가 발생할 수 있다. 파라미터로 default value를 넘겨주며 안전하게 pop하자
print(dic.pop('not_in', 'test'))
print(dic)

# 딕셔너리에 있는 모든 키들을 가져올 필요가 있다.
print(dic.keys())
# dict_keys 타입이다
# 리스트로 바꾸려면 그냥 리스트로 캐스팅하면 된다.
print(list(dic.keys()))
# value들을 가져올 수도 있다.
print(list(dic.values()))

# 딕셔너리에 딕셔너리를 추가하려면
dic2 = {'new': 141}
dic.update(dic2)
# 키와 밸류가 없으면 추가, 있으면 대체한다.
print(dic)
