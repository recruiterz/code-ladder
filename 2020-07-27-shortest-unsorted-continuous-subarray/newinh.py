class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        
        length = len(nums)
        shortest_length = length
        
        for i, n in enumerate(nums):
            if n == sorted_nums[i]:
                shortest_length -= 1
            else:
                break
                
        for l in range(shortest_length):
            if nums[length - l - 1] == sorted_nums[length - l - 1]:
                shortest_length -= 1
            else:
                break
        return shortest_length
            
            
