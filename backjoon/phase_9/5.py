"""
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '->', b)
        return
    hanoi(n - 1, a, c, b)  # b <-> c
    print(a, '->', b)
    hanoi(n-1, c, b, a)  # a <-> b , b <-> c
hanoi(3, 1, 3, 2)
"""


def hanoi(n, start, middle, target):
    if n == 1:
        print(start, middle)
        return
    hanoi(n-1, start, target, middle)
    print(start, middle)
    hanoi(n-1, target, middle, start)


n = int(input())

cnt = 0
for i in range(n):
    cnt = cnt * 2 + 1

print(cnt)
hanoi(n, 1, 3, 2)


# 전체 hanoi(3, 1, 3, 2) 호출시
"""
def hanoi(3, 1, 3, 2):
  # if n == 1:
  # print(a, '->', b)  
  hanoi(2, 1, 2, 3) [checkpoint #1]
  --------------------------------------
  def hanoi(2, 1, 2, 3):
    # if n == 1:
    #   print(a, '->', b) 
    #   return
    hanoi(1, 1, 3, 2) [checkpoint #2]
    -------------------------------------- 1 -> 3
    def hanoi(1, 1, 3, 2):
      if n == 1:
        print(a, '->', b) 
        return [back to the checkpoint #2]
  -------------------------------------- 1 -> 2
  def hanoi(2, 1, 2, 3):
    # if n == 1:
    #   print(a, '->', b) 
    #   return
    # hanoi(1, 1, 3, 2) 
    print(a, '->', b)
    hanoi(1, 3, 2, 1)
    -------------------------------------- 3 -> 2
    def hanoi(1, 3, 2, 1):
      if n == 1:
        print(a, '->', b)
        return [back to the checkpoint #1]
-------------------------------------- 1 -> 3
def hanoi(3, 1, 3, 2):
  # if n == 1:
  # print(a, '->', b)    
  # hanoi(2, 1, 2, 3)
  print(a, '->', b)
  hanoi(2, 2, 3, 1) [function of the end]
  --------------------------------------
  def hanoi(2, 2, 3, 1):
    # if n == 1:
    # print(a, '->', b)
    # return 
    hanoi(1, 2, 1, 3) [checkpoint #3]
    -------------------------------------- 2 -> 1
    def hanoi(1, 2, 1, 3)
      if n == 1:
        print(a, '->', b)
        return  [back to the checkpoint #3]
  -------------------------------------- 2 -> 3
  def hanoi(2, 2, 3, 1):
    # if n == 1:
    # print(a, '->', b)
    # return
    # hanoi(1, 2, 1, 3) 
    print(a, '->', b)
    hanoi(1, 1, 3, 2) [function of the end]
    -------------------------------------- 1 -> 3
    def hanoi(1, 1, 3, 2):
      if n == 1:
        print(a, '->', b)        
"""

# 부분 요약
# 1
"""
def hanoi(3, 1, 3, 2): 
  if n == 1:
    print(a, '->', b)
    return
  hanoi(3-1, 1, 2, 3) -> hanoi(2, 1, 2, 3) return - checkpoint
"""

# 2
"""
def hanoi(2, 1, 2, 3): 
  if n == 1:
    print(a, '->', b)
    return
  hanoi(2-1, 1, 3, 2) -> hanoi(1, 1, 3, 2) return - checkpoint
"""

# 3
"""
def hanoi(1, 1, 3, 2):
  if n == 1:
    print(a, '->', b) -> 출력: 1 -> 3
    return  -> # 2 checkpoint  
"""

# 4
"""
def hanoi(2, 1, 2, 3):
  # 2 checkpoint
  print(a, '->', b) -> 출력: 1 -> 2
  hanoi(2-1, 3, 2, 1) -> hanoi(1, 3, 2, 1) 
"""

# 5
"""
def hanoi(1, 3, 2, 1):
  if n == 1:
    print(a, '->', b) -> 출력: 3 -> 2 
    return -> # 1 checkpoint
"""

# 6
"""
def hanoi(3, 1, 3, 2):
  print(a, '->', b) -> 출력: 1 -> 3 
  hanoi(3 - 1, 2, 3, 1)
"""

# 7
"""
def hanoi(2, 2, 3, 1):
  if n == 1:
    print(a, '->', b)
    return
  hanoi(2 - 1, 2, 1, 3) -> hanoi(1, 2, 1, 3) return - checkpoint
"""

# 8
"""
def hanoi(1, 2, 1, 3):
  if n == 1:
    print(a, '->', b) -> 출력: 2 -> 1
    return -> # 7 checkpoint
"""

# 9
"""
def hanoi(2, 2, 3, 1):
  print(a, '->', b) -> 출력: 2 -> 3
  hanoi(2 - 1, 1, 3, 2) -> hanoi(1, 1, 3, 2)
"""

# 10
"""
def hanoi(1, 1, 3, 2):
  print(a, '->', b) -> 출력: 1 -> 3
  return -> 종료 
"""
