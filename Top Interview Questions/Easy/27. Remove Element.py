class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        place = 0
        compare = 0
        length = len(nums)
        while compare<length:
            if(nums[compare]!=val):
                nums[place] = nums[compare]
                place+=1
                compare+=1
            else:
                # if current compare value is equal to the undesired value we just skip it, and maintain the index/count of the other values
                compare+=1
        k = place
        while place<length:
            nums[place] = None
            place+=1

        return k
