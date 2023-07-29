def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))


"""
점화식은 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현한 것을 의미한다.

if n이 0 혹은 1일 때:
    factorial(n) = 1 
elif n이 1보다 클 때:
    factorial(n) = n * factorial(n - 1)
"""
