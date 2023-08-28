# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#
#         start = 0
#         end = 2
#         sum_n = sum(nums[start:end])
#         output = len(nums)
#
#         while start < end:
#             if sum_n < target and end < len(nums) + 1:
#                 end += 1
#             elif sum_n == target and end < len(nums) + 1:
#                 output = min(len(nums[start:end]), output)
#                 end += 1
#             else:
#                 start += 1
#             sum_n = sum(nums[start:end])
#
#
#         if output >= len(nums):
#             return 0
#
#         return output
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        l, sum = 0, 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minlen = min(minlen, r - l + 1)
                sum -= nums[l]
                l += 1

        return minlen if minlen <= len(nums) else 0


s = Solution()
# print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
# print(s.minSubArrayLen(4, [1, 4, 4]))
# print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))

