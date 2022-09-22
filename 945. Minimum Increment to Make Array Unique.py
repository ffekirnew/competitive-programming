#UNDERSTANDING 
# restate it: make the array unique by adding 1 and return the ammount of times you have added
# inputs: an int array of length between 1 and 100000
# output: an int (32 bit, 4 byte)


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # sort the numbers
        nums.sort()
        # create the object to be returned
        answer = 0
        # loop through the array and make all items unique
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i] += 1
                answer += 1
            if nums[i] < nums[i-1]:
                change = nums[i-1] - nums[i] + 1
                nums[i] += change
                answer += change
        # return the object
        return answer
