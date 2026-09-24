class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=[]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
             diff = prices[j]-prices[i]
             if (diff>0):
                profit.append(diff)
        
        if(len(profit)>0):
            return max(profit)
        else:
            return 0
        