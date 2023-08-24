
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place
        """
        result = nums1[:m] + nums2[:n]
        nums1[:m+n] = sorted(result)
        print(nums1)


s = Solution()
s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
s.merge([1], 1, [], 0)
s.merge([0], 0, [1], 1)


