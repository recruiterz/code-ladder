class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:

            lh = height[left]
            rh = height[right]

            if lh <= rh:
                max_area = max(max_area, lh * (right - left))
                left += 1
            else:
                max_area = max(max_area, rh * (right - left))
                right -= 1

        return max_area
