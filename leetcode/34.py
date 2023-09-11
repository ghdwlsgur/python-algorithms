from heapq import heappush, heappop
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(nums1)
        n = len(nums2)
        ans = []
        visited = set()
        minHeap = [(nums1[0] + nums2[0] , (0, 0))]
        visited.add((0, 0))
        while k > 0 and minHeap:
            val, (i, j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])
            if i+1 < m and (i+1, j) not in visited:
                heappush(minHeap, (nums1[i+1]+nums2[j], (i+1,j)))
                visited.add((i+1, j))
            if j+1 < n and (i, j+1) not in visited:
                heappush(minHeap, (nums1[i]+nums2[j+1], (i,j+1)))
                visited.add((i, j+1))
            k -= 1
        return ans



s = Solution()
print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print(s.kSmallestPairs([1, 2], [3], 3))