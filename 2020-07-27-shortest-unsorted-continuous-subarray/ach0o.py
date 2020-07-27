class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        _min = 0
        _max = len(nums) - 1

        start = 0
        end = len(nums) - 1

        status = [True, True]

        while any(status):
            if nums[start] == sortedNums[_min]:
                start += 1
                if end + 1 - start:
                    _min += 1
                else:
                    break
            else:
                status[0] = False
            if nums[end] == sortedNums[_max]:
                end -= 1
                if end + 1 - start:
                    _max -= 1
                else:
                    break
            else:
                status[1] = False
        return 1 + end - start
