# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i = 1
#         k = 0
#         while i < len(nums):
#             if nums[i] != nums[i-1]:
#                 k = 0
#             else:
#                 k += 1
#
#             if k >= 2:
#                 nums.remove(nums[i])
#             else:
#                 i += 1
#         print(nums)

class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for num in nums:
      if i < 2 or num != nums[i-2]:
        nums[i] = num
        i += 1
    print(nums)
    return i

s = Solution()
s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
s.removeDuplicates([1, 1, 1, 2, 2, 3])



