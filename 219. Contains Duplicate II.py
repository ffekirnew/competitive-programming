# UNDERSTANDING
# can i restate it?
    # return true if the maximum distance between any pairs of a duplicate in the list is <= k
# what are the inputs?
    # an integer array and and non-negative integer
#  what is the output?
    # a boolean value
# can it be determined?
    # yes

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # create the variables for the sliding window
        start = 0
        end = 0
        
        # create the hash map for keeping track of what is already in there
        numbers = {nums[0]:0}
        
        # loop through the list 
        while end < len(nums) - 1:
            end += 1
            
            if nums[end] in numbers and end - numbers[nums[end]] <= k:
                return True
            
            numbers[nums[end]] = end
                
        # return the object
        return False
