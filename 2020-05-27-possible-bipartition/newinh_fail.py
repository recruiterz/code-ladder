class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        visited = []
        
        for _ in range(N+1):
            visited.append(False)
        
        g = []
        for _ in range(N+1):
            
            l = []
            g.append(l)
            for _ in range(N+1):
                l.append(False)
        
        for i, j in dislikes:
            
            g[i][j] = True
            g[j][i] = True
        
        stack = [(0, i) for i in range(1, N + 1)]
        
        while stack:
            
            
            edge_number, v = stack.pop()
            

            if visited[v] is True:
                if edge_number % 2 == 1:
                    return False
            visited[v] = True
            
            l = [(edge_number + 1, i) for i, j in enumerate(g[v]) if j is True and visited[i] is False]
            stack.extend(l)
        return True
        
