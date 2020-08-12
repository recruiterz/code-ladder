from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        count_dict = defaultdict(list)

        for x in arr:
            count_dict[bin(x).count('1')].append(x)

        if len(count_dict) == 1:
            return sorted(arr)
        else:
            ans = []
            for cnt, nums in sorted(count_dict.items()):
                ans += sorted(nums)
            return ans
