class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        stack = []
        paths = []
        
        stack.append((set(), 0))
        
        while stack:
            
            path, v = stack.pop()
            path = path.copy()
            path.add(v)
            
            if not graph[v]:
                paths.append(path)
                continue

            to_go = []
            for _v in graph[v]:
                if _v in path:
                    paths.append(path)
                else:
                    to_go.append(_v)
                    
            for _to_go in to_go:
                stack.append((path, _to_go))

        return [sorted(list(p)) for p in paths]
