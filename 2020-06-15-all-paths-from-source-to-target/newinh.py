class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        N = len(graph)
        stack = []
        paths = []
        
        stack.append(([], 0))
        
        while stack:
            
            path, v = stack.pop()
            path = path.copy()
            path.append(v)
            
            if not graph[v] or v == N-1:
                paths.append(path)
                continue
                    
            for to_go in graph[v]:
                stack.append((path, to_go))

        return paths
