
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        p = re.compile('[a-zA-Z0-9]')
        l = []
        for word in list(s):
            if p.match(word):
                if word.isupper():
                    word = word.lower()
                l.append(word)

        start = 0
        end = -1
        while start <= ((len(l) // 2) - 1):
            if l[start] == l[end]:
                pass
            else:
                return False
            start += 1
            end -= 1
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))