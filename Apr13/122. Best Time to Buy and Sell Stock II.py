class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hold = -prices[0]
        cash = 0
        for price in prices[1:]:
            # cash no thing
            # cash price
            cash = max(cash, hold + price)

            # hold no thing
            # hold the price
            hold = max(hold, cash - price)
        return cash
