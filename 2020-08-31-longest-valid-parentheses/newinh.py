class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        result = [False] * len(s)
        
        for i, _s in enumerate(s):
            
            stack.append((i, _s))
            
            if len(stack) < 2:
                continue
            
            if stack[-2][1] == '(' and stack[-1][1] == ')':
                ii, ss = stack.pop()
                iii, sss = stack.pop()
                
                result[ii] = True
                result[iii] = True
        
        longest = 0
        _longest = 0
        for r in result:
            if r == True:
                _longest += 1
                longest = max(longest, _longest)
            else:
                _longest = 0

        return longest
