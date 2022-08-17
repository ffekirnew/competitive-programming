class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # since the number of items in the list nums is less than or equal to 100 bubble sort will do
        exchanges = True
        while exchanges:
            exchanges = False
            for pass_num in range(len(nums) - 1, 0, -1):
                for i in range(pass_num):
                    if nums[i] > nums[i + 1]:
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                        exchanges = True
                        
        target_indices = []
        for i in range(len(nums)):
            if nums[i] == target:
                target_indices.append(i)
        return target_indices