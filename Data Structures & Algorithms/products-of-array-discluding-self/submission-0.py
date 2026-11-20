class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        
        prefix = 1
        for i in range(n): # get everything to the left except self
            output[i] = prefix
            prefix*=nums[i]

        suffix = 1
        for i in range(n-1,-1,-1): #everything to the right except self
            output[i]*=suffix
            suffix*=nums[i]
        return output