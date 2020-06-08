from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums_c = len(nums)
        number_check = {i:0 for i in nums}
        print(number_check)
        for i in nums:
            number_check[i] += 1
            if number_check[i] > nums_c/2:
                return i
