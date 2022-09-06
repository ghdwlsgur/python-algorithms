
# ! Version: 1
# import sys
# from math import gcd
# n = int(sys.stdin.readline().rstrip())
# l = list(map(int, sys.stdin.readline().split()))

# big_circle = l[0]
# for i in range(1, n):
#     if big_circle < l[i]:
#         if l[i] % big_circle == 0:
#             print('{}{}{}'.format(1, "/", l[i]//big_circle))
#         else:
#             print('{}{}{}'.format(big_circle, "/", l[i]))
#     else:
#         if round(big_circle / l[i]) == big_circle / l[i]:
#             print('{}{}{}'.format(int(big_circle/l[i]), '/', 1))
#         else:
#             decimal_point = len(
#                 str(big_circle/l[i])) - len(str(round(big_circle/l[i]))) - 1
#             a = int(big_circle/l[i] * (10 * decimal_point))
#             b = (10 * decimal_point)
#             print('{}{}{}'.format(int(a) // gcd(a, b), "/", int(b) // gcd(a, b)))


# ! Version: 2
# import sys
# from fractions import Fraction

# n = int(sys.stdin.readline().rstrip())
# l = list(map(int, sys.stdin.readline().split()))

# t = l[0]
# for i in range(1, len(l)):
#     if t % l[i] == 0:
#         print(f'{int(t // l[i])}/1')
#     else:
#         print(Fraction(t, l[i]))


# import sys
# from fractions import Fraction 
# n = int(sys.stdin.readline().rstrip())
# l = list(map(int, sys.stdin.readline().split()))


# t = l[0]
# for i in range(1, len(l)):
#     if t % l[i] == 0:
#         print(f'{int(t // l[i])}/1')
#     else:
#         print(Fraction(t, l[i]))
        
        
import sys 
from fractions import Fraction
n = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().split()))

t = l[0]
for i in range(1, len(l)):
    if t % l[i] == 0:
        print(f'{int(t // l[i])}/1')
    else:
        print(Fraction(t, l[i]))

