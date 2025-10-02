class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        point1_lowest: int = prices[0]
        max_profit: int = 0

        for idx in range(1, len(prices)):
            if prices[idx] < point1_lowest:
                point1_lowest = prices[idx]
            
            max_profit = max(max_profit, prices[idx] - point1_lowest)
        
        return max_profit

print(Solution().maxProfit([7, 1, 5, 3, 6, 4])) # 5
print(Solution().maxProfit([7,6,4,3,1])) # 0
print(Solution().maxProfit([2,4,1,11,7])) # 10
print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0])) # 8
