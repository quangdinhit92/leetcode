class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        k =2 
        states = [0] + [-float('inf') for i in range(2*k)]
        states[1] =-prices[0]

        for i in range(1,n):
            for j in range (k):
                states[2*j+1] = max(states[2*j+1],states[2*j] -prices[i] )
                states[2*j+2] = max(states[2*j+2],states[2*j+1]+prices[i])
        return max(0,states[-1])