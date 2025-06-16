class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            leftOverTarget = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == leftOverTarget:
                   return [i,j]