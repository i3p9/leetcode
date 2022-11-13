class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        """
        day0 -> we have our current buy price
        loop normally to find if we can find a buy price lower than our current one
        if we can find, then we set the buy price to the newly found lower one
        if not, maybe we can sell, so we calculate our potential profit
        and check if that potential profit is more than our max profit
        if yes -> max profit is now the potential profit, if not
        do nothing

        the same thing can be done looping backwards, where we'll set the sell price first
        """

        for i in range(len(prices)):
            if prices[buy] > prices[i]: #ohno, we can buy a lower price stock
                buy = i

            else:
                maybe_profit = prices[i] - prices[buy]
                if maybe_profit > max_profit:
                    max_profit = maybe_profit

        return max_profit
