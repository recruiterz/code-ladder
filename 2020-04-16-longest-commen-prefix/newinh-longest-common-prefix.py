class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_str = ''
        min_length = float("inf") 
        for str in strs:
            if len(str) < min_length:
                min_str = str
                min_length = len(str)
        
        
        for i, s in enumerate(min_str):
            
            for str in strs:
                if s != str[i]:
                    return min_str[:i]
        
        return min_str

