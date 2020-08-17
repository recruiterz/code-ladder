from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_counter = Counter(p)
        
        def is_anagram(slice_s) -> bool:
            c = Counter(slice_s)
            
            if len(p_counter) != len(c):
                return False
            
            for k in c.keys():
                if c[k] != p_counter.get(k, 0):
                    return False
            return True
        
        len_p = len(p)
        len_s = len(s)
        
        output = []
        for i in range(0, len_s - len_p + 1):
            if is_anagram(s[i:i+len_p]):
                output.append(i)
        return output
