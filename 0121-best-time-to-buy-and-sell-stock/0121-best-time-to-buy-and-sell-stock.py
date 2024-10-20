class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = int(1e4+1)
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit