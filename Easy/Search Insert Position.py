class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high, pos = 0, len(nums)-1, -1
        while low <= high:
            mid = int(low+(high-low)/2)
            if nums[mid] == target: return mid
            if(nums[mid] < target):
                low = mid + 1
                pos = mid + 1
            else:
                pos = mid
                high = mid - 1
        return pos
