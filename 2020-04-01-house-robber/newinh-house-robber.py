class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        
        d = []
        d.append(nums[0])
        d.append(max(nums[0], nums[1]))
        
        
        for i in range(2, len(nums)):
            d.append(max(d[i-1], d[i-2] + nums[i]))
        
        return d[-1]
        

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        
        a, b = nums[0], max(nums[0], nums[1])
        
        
        for i in range(2, len(nums)):
            a, b = b, max(a + nums[i], b)
        
        return b
