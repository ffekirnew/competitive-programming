class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True) # since it is a sorting problem

        # to optimize since the values we need are at the first and second second positions of the piles 
        index = 2
        for i in range(len(piles) // 3):
            piles.insert(index, piles.pop())
            index += 3
            
        result = 0
        for i in range(1, len(piles), 3):
            result += piles[i]
            
        return result
        