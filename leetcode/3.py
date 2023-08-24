
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         memory = nums[0]
#         k = 1
#         for i in range(1, len(nums)):
#             if memory != nums[i]:
#                 nums[k] = nums[i]
#                 k += 1
#                 memory = nums[i]
#         return k

class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 1
    while i < len(nums):
      if nums[i] == nums[i-1]: # 현재 인덱스가 이전 인덱스와 같을 경우
        nums.remove(nums[i]) # 현재 인덱스 요소를 제거
      else:
        i += 1 # 같지 않을 경우 1 증가
    print(nums)

s = Solution()
s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])






