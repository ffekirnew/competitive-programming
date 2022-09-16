class Solution:            
    def findDuplicate(self, nums: List[int]) -> int:
        freqDict = {i: 0 for i in range(1, len(nums))}
        for i in nums:
            if freqDict[i] > 0:
                return i
            else:
                freqDict[i] += 1
