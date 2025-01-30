class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time = O(n)
        # Space = O(n)
        # pre, post, final = ([1] * len(nums) for _ in range(3))
        # pre[-1], post[-1] = nums[-1], nums[-1]
        # pre[0], post[0],  = nums[0], nums[0]
        # for i in range(1,len(nums)):
        #     pre[i] = pre[i-1]*nums[i]
        # for i in range(len(nums)-2,0,-1):
        #     post[i] = post[i+1]*nums[i]
        # for i in range(1,len(nums)-1):
        #     final[i] = pre[i-1]*post[i+1]

        # final[-1] = pre[-2]
        # final[0] = post[1]
        # return final
        
        # Time = O(n)
        # Space = O(1)

        # pre = [1] * len(nums)
        # pre[0]  = nums[0]
        # for i in range(1,len(nums)):
        #     pre[i] = pre[i-1]*nums[i]
        # for i in range(len(nums)-2,0,-1):
        #     nums[i] = nums[i+1]*nums[i]
        # last = pre[-2]
        # first = nums[1]
        # for i in range(1,len(nums)-1):
        #     nums[i] = pre[i-1]*nums[i+1]
        # nums[0] = first
        # nums[-1] = last
        # return nums


        # Time = O(n) 2 passes instead of 3 passes
        # Space = O(1) (output not included)

        pre = [1] * len(nums)
        pre[0]  = nums[0]
        accumalatePost = 1
        for i in range(1,len(nums)):
            pre[i] = pre[i-1]*nums[i]

        for i in range(len(nums)-1,0,-1):
            temp = accumalatePost * pre[i-1]
            accumalatePost = nums[i] * accumalatePost
            nums[i] = temp
            
        nums[0] = accumalatePost
        return nums
        