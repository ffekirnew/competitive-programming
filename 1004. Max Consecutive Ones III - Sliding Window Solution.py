class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # create the object to be returned
        answer = 0
        # set up the sliding window
        start = 0
        end = 0
        # keep the count of flips made
        flips = 0
        # loop through the nums
        while end < len(nums):
            if nums[end] == 1: end += 1
            else:
                if flips < k:
                    end += 1
                    flips += 1
                else:
                    if nums[start] == 0: 
                        flips -= 1
                    elif start == end: 
                        end += 1
                    start += 1
            answer = max(answer, end - start)
        # return the solution
        return answer
