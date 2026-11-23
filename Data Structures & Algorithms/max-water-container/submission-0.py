class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        most = 0
        while left < right:
            lowest = min(heights[left], heights[right])
            most = max(most, lowest * (right - left))
            if heights[left] <heights[right]:
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else:
                left+=1
                right-=1
        return most