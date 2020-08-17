from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def is_anagram(c1, c2) -> bool:
            if len(c1) != len(c2):
                return False
            
            for k in c1.keys():
                if c1[k] != c2.get(k, 0):
                    return False
            return True
            
        
        len_p = len(p)
        len_s = len(s)
        
        p_counter = Counter(p)
        s_counter = Counter(s[:len_p])
        
        output = []
        for i in range(0, len_s - len_p + 1):
            if i != 0:
                sliced_s_to_delete = s[i-1]
                s_counter[sliced_s_to_delete] -= 1
                if s_counter[sliced_s_to_delete] == 0:
                    s_counter.pop(sliced_s_to_delete)
                
                sliced_s_to_add = s[i + len_p - 1]
                count = s_counter.setdefault(sliced_s_to_add, 0)
                s_counter[sliced_s_to_add] = count + 1
                
            if is_anagram(p_counter, s_counter):
                output.append(i)
        return output
