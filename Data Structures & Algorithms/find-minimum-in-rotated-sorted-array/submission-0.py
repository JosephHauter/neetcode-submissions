class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search to find lowest number
        # check middle and if middle > left pointer index 0 search right
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left+right) //2
            # Check if mid element is greater than the rightmost element
            if nums[mid] > nums[right]:
                left = mid+1
            
             # Check if mid element is less than the rightmost element
            elif nums[mid] < nums[right]:
                right = mid
            # If mid element and rightmost element are equal, move the right pointer towards left
            else:
                right-=1
                # At the end of the loop, left and right will point to the minimum element
        return nums[left]