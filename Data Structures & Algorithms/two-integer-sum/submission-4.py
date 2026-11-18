class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1,-1,-1):
        #         for j in range(i-1,-1,-1):
        #             if nums[i]+nums[j]==target:
        #                 return [j,i]
        # return [0,0]
        mapN = {}
        for i in range(len(nums)):
            if nums[i] not in mapN:
                mapN[target-nums[i]] = i
            else:
                return [mapN[nums[i]], i]