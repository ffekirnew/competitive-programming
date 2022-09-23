class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # create a pointer to keep track of where to put the non zeros
        pointer = 0
        # loop through nums and move all non-zeros to the front in order
        for num in nums:
            if num != 0:
                nums[pointer] = num
                pointer += 1
        # since everything is ruined now, make all elements starting from j zero
        while pointer < len(nums):
            nums[pointer] = 0
            pointer += 1
