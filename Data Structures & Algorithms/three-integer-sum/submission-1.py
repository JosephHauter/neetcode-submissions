class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        size = len(nums)
        for i, num in enumerate(nums):
            if num> 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low, high = i+1, size-1
            while low < high:
                calc = num+ nums[low]+nums[high]
                if calc == 0:
                    output.append([num,nums[low],nums[high]])
                    low+=1
                    high-=1
                    while nums[low] ==nums[low-1] and low < high:
                        low+=1
                elif calc > 0:
                    high-=1
                elif calc < 0:
                    low+=1
        return output
                