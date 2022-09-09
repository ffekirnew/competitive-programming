class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices[:]
        stack = []
        
        for i in range(len(prices) - 1, -1, -1):
            curr = prices[i]
            
            while stack and curr < stack[-1]:
                stack.pop()
            
            if stack:
                result[i] = curr - stack[-1]
                
            stack.append(curr)
        
        return result
