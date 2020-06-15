class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def DFS(node):
            #base case: last element
            if node == len(graph)-1: 
                print([[node]])
                return [[node]]
            paths = []
            for prev in graph[node]:
                for path in DFS(prev):
                    print(path)
                    paths.append([node] + path)
            return paths
        return DFS(0)
