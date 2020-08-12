class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        diff = []
        for n, i in enumerate(nums):
            if sorted_nums[n] != i:
                diff.append(n)
        if not diff:
            return 0
        return diff[-1] - diff[0] + 1

#  brute force time limit exceeded
# class Solution:
#     def findUnsortedSubarray(self, nums) -> int:
#         l, r = len(nums), 0
#         for i in range(len(nums)):
#             for j in reversed(range(i)):
#                 if nums[j] > nums[i]:
#                     l = min(l, j)
#                     r = max(r, i)
# 
#         min_len = max(0, r - l + 1)
#         return min_len
