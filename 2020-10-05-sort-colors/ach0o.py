class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pt = 0
        size = len(nums)

        while pt < size - 1:
            if nums[pt] > nums[pt+1]:
                nums[pt], nums[pt+1] = nums[pt+1], nums[pt]
                pt -= 1
                if pt < 0:
                    pt = 0
            else:
                pt += 1
        return nums
