from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            # 필요한 숫자 추출
            # print(nums[i])
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i


        return []

s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))