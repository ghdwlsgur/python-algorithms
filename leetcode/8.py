class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        max_profit = 0
        sum = 0
        while right < len(prices):
            cur_profit = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit = max(cur_profit, max_profit)
                left = right

            else:
                left = right
            right += 1

        print(sum)
        return max_profit

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
# print(s.maxProfit([1, 2, 3, 4, 5]))
# print(s.maxProfit([7, 6, 4, 3, 1]))


