class Solution:
    
    def is_valid(self, s: str) -> bool:
        stack = []
        
        for i, _s in enumerate(s):
            if _s not in ['(', ')']:
                continue
            stack.append((i, _s))
            
            if len(stack) > 1 and stack[-2][1] == '(' and stack[-1][1] == ')':
                stack.pop()
                stack.pop()

        if stack:
            return False
        return True
        
        
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stack = []
        
        for i, _s in enumerate(s):
            if _s not in ['(', ')']:
                continue
            stack.append((i, _s))
            if len(stack) > 1 and stack[-2][1] == '(' and stack[-1][1] == ')':
                stack.pop()
                stack.pop()
        if not stack:
            return [s]
        
        d = {}
        
        for i, _s in stack:
            d[i] = [i]
            
            
        for i, removable_indexes in d.items():
            
            if s[i] == ')':
                for _i, _s in enumerate(s[:i]):
                    if _s == ')':
                        removable_indexes.append(_i)
            elif s[i] == '(':
                for _i, _s in enumerate(s[i:]):
                    if _i == i:
                        continue

                    if _s == '(':
                        removable_indexes.append(_i)
                        
        total_possibility = 1
        for i, removable_indexes in d.items():
            total_possibility *= len(removable_indexes)
            
        count = len(d)
        
        total_removable_indexes = []
        for _ in range(total_possibility):
            _a = [None, ] * count
            total_removable_indexes.append(_a)
        
        for i, removable_indexes in enumerate(d.values()):
            index_count = len(removable_indexes)
            
            for j, t in enumerate(total_removable_indexes):
                t[i] = removable_indexes[j % index_count]
        
        
        result = set()
        for tps in total_removable_indexes:
            if len(set(tps)) != count:
                continue
                
            l = [a for a in s]
            for i in tps:
                l[i] = None
        
            ss = ''.join([a for a in l if a])
            if self.is_valid(ss):
                result.add(ss)
        
        return list(result)
        
    

