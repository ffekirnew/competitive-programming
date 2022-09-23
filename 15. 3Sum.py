class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create the empty result object
        results = []
        # sort the nums list
        nums.sort()
        if nums[0] == nums[-1] == 0:
            return [[nums[0]] * 3]
        # create three pointers, one in front, one at the end, one in the middle and loop through the nums list
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                threeNums = [nums[i], nums[j], nums[k]]
                
                if nums[i] + nums[j] + nums[k] == 0:
                    results = results + [threeNums] if (not threeNums in results) else results
                    k -= 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
                    
        # return the result
        return results
