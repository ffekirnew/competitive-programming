class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        i = 0
        prefix = 0
        postfix = total - nums[i]
        while i < len(nums):
            if prefix == postfix:
                return i
            prefix += nums[i]
            i += 1
            postfix = postfix - nums[i] if i < len(nums) else 0
            
        return -1
