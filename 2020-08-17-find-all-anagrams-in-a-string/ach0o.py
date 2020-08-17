class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        char = []
        _p = sorted(p)
        index = 0

        for c in s:
            char.append(c)

            if len(char) == len(p):
                if sorted(char) == _p:
                    ans.append(index)
                char.pop(0)
                index += 1

        return ans
