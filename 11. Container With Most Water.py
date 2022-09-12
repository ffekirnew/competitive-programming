class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        result = 0
        area = 0
        
        while j > i:
            if height[i] > height[j]:
                area = (j - i) * height[j]
                j -= 1
            else:
                area = (j - i) * height[i]
                i += 1
            
            if area > result:
                result = area
        
        return result
