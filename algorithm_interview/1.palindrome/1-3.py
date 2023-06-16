import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


if __name__ == "__main__":
    solution = Solution()
    result = solution.isPalindrome("A man, a plan, a canal: Panama")
    print(result)
    result = solution.isPalindrome("race a car")
    print(result)
    result = solution.isPalindrome(" ")
    print(result)
