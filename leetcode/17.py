class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = []
        for row in matrix:
            for i in row:
                l.append(i)

        start = 0
        end = len(l) - 1

        while start <= end:
            mid = (start + end) // 2

            if l[mid] > target:
                end = mid - 1
            elif l[mid] < target:
                start = mid + 1
            else:
                return True

        return l[start] == target



s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(s.searchMatrix([[1]], 2))
print(s.searchMatrix([[1, 1]], 2))