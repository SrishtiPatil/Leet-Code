class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n_max, sub_max = nums[0], 0
        if len(nums) == 1: return n_max
        for i in nums:
            sub_max = max(i, sub_max + i)
            n_max = max(sub_max, n_max)
        return n_max
