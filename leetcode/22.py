class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(set(ransomNote)) == len(magazine):
            return False

        alphaMap = {}

        for value in ransomNote:
            if value in alphaMap:
                alphaMap[value] += 1
            else:
                alphaMap[value] = 1

        for value in magazine:
            if value in alphaMap:
                alphaMap[value] -= 1

        for i in alphaMap.values():
            if i > 0:
                return False

        return True


s = Solution()
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "aab"))
print(s.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))
