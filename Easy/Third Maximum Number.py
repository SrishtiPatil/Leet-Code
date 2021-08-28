class Solution:
  def thirdMax(self, nums: List[int]) -> int:
      from collections import Counter
      n = len(nums)
      temp = -sys.maxsize
      i, j, k = temp, temp, temp
      if n == 1:
          return nums[0]
      if nums[0] > nums[1]:
          i = nums[0]
          j = nums[1]
      else:
          j = nums[0]
          i = nums[1]
      if i == j:
          j = temp
      for t in range(2,n):
          if i == nums[t] or j == nums[t] or k == nums[t]:
              continue
          elif nums[t] > i:
              k = j
              j = i
              i = nums[t]
          elif nums[t] < i  and nums[t] > j:
              k = j
              j = nums[t]
          elif nums[t] < j and nums[t] > k:
              k = nums[t]
      if n == 2 or len(Counter(nums)) < 3:
          return i
      return k
