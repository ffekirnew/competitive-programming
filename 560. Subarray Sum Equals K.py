Solution to 560. Subarray Sum Equals K at LeetCodeclass Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force
        # for i in range(len(nums)):
        #     curr = 0
        #     for j in range(i, len(nums)):
        #         curr += nums[j]
        #         if curr == k: answer += 1
        #         if curr >= k: break

        # sliding window optimization (won't work since there will be negative values in the array)
        # s = 0
        # e = 0
        # curr = 0
        # while e < len(nums):
        #     curr += nums[e]
        #     e += 1
        #     while curr >= k:
        #         answer += 1 if (curr == k) else 0
        #         curr -= nums[s]
        #         s += 1

        # create the object to be returned
        answer = 0
        # find the prefix sum and store it in a hashmap
        curr = 0
        prefix_map = {0:1}
        for num in nums:
            curr += num
            if (curr - k) in prefix_map:
                answer += prefix_map[(curr - k)]
            prefix_map[curr] = 1 if (not curr in prefix_map) else prefix_map[curr] + 1

        # return the object
        return answer
