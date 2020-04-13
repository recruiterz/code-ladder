from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        
        for n, l in d.items():
            
            if target - n in d:
                
                if len(d[target - n]) == 1 and l[0] != d[target - n][0]:
                    return [l[0], d[target - n][0]]
                if len(d[target - n]) > 1:
                    return [l[0], d[target - n][1]]
