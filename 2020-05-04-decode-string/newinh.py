class Solution:
    def decodeString(self, s: str) -> str:
        
        
        stack = []
        
        
        for _s in s:
            
            
            if _s == ']':
                
                to_repeat = ''
                while stack[-1].isalpha():
                    to_repeat = stack.pop() + to_repeat
                    
                stack.pop() # remove [
                count = ''
                while stack and stack[-1].isnumeric():
                    count = stack.pop() + count
                
                count = int(count)
                
                
                repeated = count * to_repeat
                stack.append(repeated)
            else:
                stack.append(_s)
        
        result = ''
        while stack:
            result = stack.pop() + result
            
        return result

