class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums] # since there will be a lot of concatenation

        #then it is essentially a sorting problem, used the insertion sort in my case to try and insert the strings onto their correct positions by comparing which combination gives the larger number
        for i, n in enumerate(nums):
            item = n
            c = i
            while c > 0 and nums[c - 1] + item <= item + nums[c - 1]:
                c -= 1
            nums.insert(c, nums.pop(i))
        
        # run into an error that i will need to delete all leading zeros so
        while nums[0] == "0" and len(nums) > 1:
            nums.pop(0)
        
        # return a single string
        return "".join(nums)