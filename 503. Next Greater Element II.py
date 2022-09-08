class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums += nums[:len(nums)-1]
        stack, result = [], [-1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            current_num = nums[i]
            if stack == []: stack.append(current_num)
            else:
                while stack and stack[-1] <= current_num:
                    stack.pop()
                
                if stack != []: result[i] = stack[-1]
                stack.append(current_num)
                    
        return result[:n]
