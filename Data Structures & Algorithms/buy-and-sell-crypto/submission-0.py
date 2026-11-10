class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], prices[0]
        profit = 0

        for p in prices:
            if p < buy:
                profit = max(profit, sell - buy)
                buy, sell = p, p
            elif p > sell:
                sell = p
            
        
        return max(profit, sell-buy)

        