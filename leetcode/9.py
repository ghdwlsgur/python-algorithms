class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        bucket = [0]
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        for i in range(0, len(nums)-1):
            if i == 0:
                for j in range(0, nums[i]):
                    bucket.append(0)
                if len(bucket) >= len(nums):
                    return True
                continue

            arange = (i + 1) + nums[i]

            if i + 1 == len(bucket) and nums[i] == 0:
                return False

            if len(bucket) < arange:
                k = arange - len(bucket)
                for j in range(k):
                    bucket.append(0)

        if len(bucket) >= len(nums):
            return True
        else:
            return False


s = Solution()
# print(s.canJump([0]))
# print(s.canJump([1, 1, 1, 0])) # True
# print(s.canJump([1, 1, 0, 1])) # False
# print(s.canJump([0, 1]))
# print(s.canJump([1, 2]))
# print(s.canJump([3, 3, 1, 0, 4]))
# print(s.canJump([2, 3, 1, 1, 4]))
# print(s.canJump([3, 2, 1, 0, 4]))
print(s.canJump([1, 0, 1, 0]))
print(s.canJump([2, 3, 1, 1, 4]))

