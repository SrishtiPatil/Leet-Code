class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        ans = []
        for i in range(len(nums)):
            n2 = target - nums[i]
            if n2 in temp.keys():
                n2_index = nums.index(n2)
                if(i != n2_index):
                    return sorted([i, n2_index])
            temp.update({nums[i]:i})
