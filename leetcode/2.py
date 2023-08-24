# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#
#         k = 0
#         for n in nums[:]:
#             if n == val:
#                 nums.remove(n)
#             else:
#                 k += 1
#         return k


# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#
#         k = 0
#         index_arr = []
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 index_arr.append(i)
#             else:
#                 k += 1
#
#         lst_index = len(nums)-1
#         for i in range(len(index_arr)-1, -1, -1):
#             if index_arr[i] == lst_index:
#                 lst_index -= 1
#             else:
#                 nums[index_arr[i]], nums[lst_index] = nums[lst_index], nums[index_arr[i]]
#                 lst_index -= 1
#         return k

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        print(nums)
        return i


s = Solution()
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
# print(s.removeElement([3, 2, 2, 3], 3))