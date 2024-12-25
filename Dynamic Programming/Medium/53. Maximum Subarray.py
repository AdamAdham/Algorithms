class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = nums[0]
        temp = nums[0]
        
        for i in range(1,len(nums)):
            temp = max(nums[i],temp + nums[i])
            maxim = max(maxim,temp)
            
        return maxim      