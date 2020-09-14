class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums)
        idx = None
        while lo < hi:
            mid = (hi + lo) // 2

            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] > target:
                hi = mid
            else:  # mid < target
                lo = mid + 1

        if idx is not None:
            _min = None
            for i in range(idx, -1, -1):
                if nums[i] == target:
                    _min = i
                else:
                    break

            _max = None
            for i in range(idx, len(nums)):
                if nums[i] == target:
                    _max = i
                else:
                    break
            return [_min, _max]
        else:
            return [-1, -1]
