
# class Solution(object):
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l = []
#
#         if len(s) > 0:
#             word = s[0]
#             if len(s) == 1:
#                 return 1
#         else:
#             word = ""
#
#         ll = list(s)
#         for i in range(1, len(s)):
#             if ll[i] not in word:
#                 word += ll[i]
#             else:
#                 word = ll[i]
#             l.append(word)
#
#         print(l)
#         maxlen = 0
#         for word in l:
#             maxlen = max(len(word), maxlen)
#
#         return maxlen

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return maxLength


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
# print(s.lengthOfLongestSubstring("bbbbb"))
# print(s.lengthOfLongestSubstring("pwwkew"))
# print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("dvdf"))