class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n_0 = 0
        n_1 = 0
        
        for i in nums:
            if i == 0:
                n_0 += 1
            elif i == 1:
                n_1 += 1
                
        for i in range(len(nums)):
            
            if i < n_0:
                nums[i] = 0
            elif n_0 <= i < n_0 + n_1:
                nums[i] = 1
            else:
                nums[i] = 2
