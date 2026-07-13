class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            water = (right - left)*min(heights[right], heights[left])
            maxArea = max(maxArea, water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        return maxArea