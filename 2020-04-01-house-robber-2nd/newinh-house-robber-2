class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        

        # 첫번째 집 제외
        _nums = nums.copy()
        _nums.pop(0)
        
        a, b = _nums[0], max(_nums[0], _nums[1])
        
        for i in range(2, len(_nums)):
            a, b = b, max(a + _nums[i], b)
            
        # 마지막 집 제외
        c, d = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            c, d = d, max(c + nums[i], d)
            
        return max(b, d)
