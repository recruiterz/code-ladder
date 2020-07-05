class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        
        projects = []
        
        for p, c in zip(Profits, Capital):
            projects.append((p, c))
            
        
        projects.sort(key=lambda i: (-i[0], i[1]))
        
        for _ in range(k):
            for i, (p, c) in enumerate(iter(projects)):
                
                if c <= W:
                    W += p
                    projects.pop(i)
                    break
        return W

