#UNDERSTANDING
# restate it: find all subarrays in the array with product less than k
# inputs: an intgeer array with length >= 1, and another integer
# output: an integer
# can the solution be determined determined: yes

# BREAK THE PROBLEM DOWN
# naive soluiton: iterate over the array for each item iterating over the contiguous elements finding the products untill failure is faced - O(n^2)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # create the object to be returned
        answer = 0
        # create the variables to set the sliding window
        start = 0
        end = 0
        curr_product = 1
        # loop through the array and extend
        while end < len(nums):
            curr_product *= nums[end]
            end += 1
            # retract
            while curr_product >= k and start < end:
                curr_product /= nums[start]
                start += 1
            if curr_product < k:
                answer += (end - start)
        # return the object
        return answer
