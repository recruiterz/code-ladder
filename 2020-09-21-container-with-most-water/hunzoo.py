class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height) - 1
        ans = 0
        while left_idx < right_idx:
            h = min(height[left_idx], height[right_idx])
            w = right_idx - left_idx
            ans = max(ans, w * h)
            if height[left_idx] >= height[right_idx]:
                right_idx -= 1
            else:
                left_idx += 1
        return ans
