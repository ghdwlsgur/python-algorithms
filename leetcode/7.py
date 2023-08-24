class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start = 0
        end = -1
        margin = 0
        tot_days = len(prices)
        while end + tot_days > 0:
            if tot_days + end == start:
                start = 0
                end -= 1
                continue

            if prices[end] > prices[start]:
                if margin < (prices[end] - prices[start]):
                    margin = prices[end] - prices[start]
            start += 1

        return margin



s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit([2, 1, 2, 0, 1]))