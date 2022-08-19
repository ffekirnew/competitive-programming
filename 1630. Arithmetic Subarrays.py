class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        queries: int = len(l)
        result = [True] * queries
        
        for i in range(queries):
            sub_array = nums[l[i]:r[i] + 1]
            sub_array.sort()
            
            c_diff = sub_array[1] - sub_array[0]
            for j in range(2, len(sub_array)):
                if sub_array[j] - sub_array[j - 1] != c_diff:
                    result[i] = False
                    
        return result