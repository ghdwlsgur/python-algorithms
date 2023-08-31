class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numMap = {}

        for i in range(len(nums)):
            if nums[i] in numMap:
                j = numMap[nums[i]]
                if abs(i - j) <= k:
                    return True
            numMap[nums[i]] = i

        return False

s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
