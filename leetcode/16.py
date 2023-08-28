class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return start


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 4))

