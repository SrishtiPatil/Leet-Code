class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        from collections import Counter
        n = len(nums)
        c = 0
        if n == 2:
            return True
        if len(Counter(nums)) < n-1:
            return False
        if len(Counter(nums)) == n-1 and n == 3:
            return True
        i = 0
        j = 0
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                c += 1
                j = i
            if c > 1:
                return False
        if c == 0:
            return True
        if j == 0 or j == n-2:
            return True
        if nums[j-1] < nums[j+1]:
            return True
        try:
            if nums[j] < nums[j+2]:
                return True
        except:
            pass
        return False
