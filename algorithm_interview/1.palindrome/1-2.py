import collections
from typing import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    result = solution.isPalindrome("A man, a plan, a canal: Panama")
    print(result)
    result = solution.isPalindrome("race a car")
    print(result)
    result = solution.isPalindrome(" ")
    print(result)
