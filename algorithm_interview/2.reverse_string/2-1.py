from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)


if __name__ == "__main__":
    solution = Solution()
    result = solution.reverseString(["h", "e", "l", "l", "o"])
