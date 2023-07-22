


test = {
    'Good': lambda x: x**2,
    'Bad': lambda y: y%2
}

print(test['Good'](int(4)))
print(test['Bad'](int(10)))

math = [
    lambda a: a + 2,
    lambda a: a - 2,
    lambda a: a * 2,
    lambda a: a // 2
]

for e in math:
    print(e(int(10)))

print(math[1](int(2)))

mathDict = {
    "add": lambda a: a + 2,
    "sub": lambda a: a - 2,
    "multi": lambda a: a * 2,
    "div": lambda a: a // 2
}

print(mathDict["add"](int(10)))