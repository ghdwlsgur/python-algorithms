class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) > len(t):
            return False

        alphaMap = {}

        for word in s:
            if word in alphaMap:
                alphaMap[word] += 1
            else:
                alphaMap[word] = 1

        for word in t:
            if word in alphaMap:
                alphaMap[word] -= 1
            else:
                alphaMap[word] = 1

        for repeat_count in alphaMap.values():
            if repeat_count != 0:
                return False

        return True



s = Solution()
# print(s.isAnagram("anagram", "nagaram"))
# print(s.isAnagram("ratk", "car"))
print(s.isAnagram("a", "ab"))
