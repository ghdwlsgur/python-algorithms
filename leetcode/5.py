# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dic = dict()
#         for i in list(set(nums)):
#             dic[i] = 0
#             for j in nums:
#                 if i == j:
#                     dic[i] += 1
#
#         max_num = 0
#         result = 0
#         for k, v in dic.items():
#             if max_num < v:
#                 max_num = v
#                 result = k
#
#         return result


class Solution(object):
  def majorityElement(self, nums):
    nums.sort()
    return nums[len(nums)//2]

s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([3, 3, 4]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([1, 1, 1, 4, 4, 10, 10, 10, 10, 10, 10]))