class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        place = 1
        prev = nums[0]
        for compare in range(1,len(nums)):
            if(nums[compare]==prev):
                if(count<2):
                    nums[place] = nums[compare]
                    count+=1
                    place+=1
                # If already number of occurences is 2 we just ignore the value
            else:
                # prev value not equal to current so we are at a new value, so reset
                prev = nums[compare]
                count=1
                nums[place] = nums[compare]
                place+=1
        k = place
        while place<len(nums):
            nums[place] = None
            place+=1
        return k          