class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights) - 1

        while left < right:
            curr_area = (right - left) * min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            res = max(res, curr_area)
        return res