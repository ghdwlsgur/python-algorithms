import math
print(','.join(['a', 'b', 'cde']))
print('a,b,cde'.split(','))
departure, _, arrival = "Seattle-seoul".partition('-')
print(departure)
print(_)
print(arrival)


a = "Name: {}, Age: {}"
print(a.format("철수", 13))
b = "Name: 영희, Age: 15"
print(b.format("영희", 15))
c = "Name: {0}, Age: {1}: {0}의 나이가 {1}"
print(c.format("민호", 17))
d = "Name: {name}, Age: {age}: {name}의 나이가 {age}"
print(d.format(age=19, name='재석'))

pos = [12.5, 35, 90]
print("A의 좌표는 x = {p[0]}, y= {p[1]}, z = {p[2]}".format(p=pos))

print("수학에서 파이 = {m.pi}".format(m=math))
print("수학에서 파이 = {m.pi:.3f}".format(m=math))

alphabet = "abcDef"
print(alphabet.capitalize())

s = " abc  "
print(s.strip())
