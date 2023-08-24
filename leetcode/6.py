from collections import deque

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        dq = deque(nums)

        if k > 0:
            dq.appendleft(0)

        for i in range(0, k):
            dq[0], dq[-1] = dq[-1], dq[0]
            dq.pop()
            if i != k - 1:
                dq.appendleft(0)

        for i in range(len(nums)):
            nums[i] = dq[i]

        return nums


s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(s.rotate([-1, -100, 3, 99], 2))