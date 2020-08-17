from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []

        p_cnts = Counter(p)
        p_size = len(p)

        ana_candidate = s[:len(p)]
        cand_cnts = Counter(ana_candidate)

        index = 0
        for c in s[p_size:]:
            if p_cnts == cand_cnts:
                ans.append(index)

            if cand_cnts[s[index]] == 1:
                del cand_cnts[s[index]]
            else:
                cand_cnts[s[index]] -= 1
            cand_cnts[c] += 1
            index += 1

        if p_cnts == cand_cnts:
            ans.append(index)
        return ans
