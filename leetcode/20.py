from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numMap = {}
        # for i in range(len(nums)):
        #     total = target - nums[i]
        #     if total in numMap:
        #         return [numMap[total], i]
        #     numMap[nums[i]] = i
        numMap = {}
        for i in range(len(nums)):
            total = target - nums[i]
            if total in numMap:
                return [numMap[total], i]
            numMap[nums[i]] = i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))