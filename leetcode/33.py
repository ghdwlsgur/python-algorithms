# from heapq import nlargest
#
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         return nlargest(k, nums)
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         min_value = min(nums) # 6
#         max_value = max(nums) # 1
#         # 6 - 1 + 1 = 6
#         # count = [0, 0, 0, 0, 0, 0]
#         count = [0] * (max_value - min_value + 1)
#
#         for num in nums:
#             count[num - min_value] += 1
#             # [0, 0, 1, 0, 0, 0]
#             # [0, 1, 1, 0, 0, 0]
#             # [1, 1, 1, 0, 0, 0]
#             # [1, 1, 1, 0, 1, 0]
#             # [1, 1, 1, 0, 1, 1]
#             # [1, 1, 1, 1, 1, 1]
#
#         remain = k
#         # 2
#         # 2 - 1 = 1 # num = 5
#         # 1 - 1 = 0 # num = 4 -> return 4 + 1 = 5
#         for num in range(len(count) - 1, -1, -1):
#             remain -= count[num]
#             if remain <= 0:
#                 print(num)
#                 return num + min_value
#         return -1

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                k = heapq.heappop(heap)

        return heap[0]


s = Solution()
print(s.findKthLargest([1, 3, 5, 4, 8, 7], 3))
# print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)[-1])