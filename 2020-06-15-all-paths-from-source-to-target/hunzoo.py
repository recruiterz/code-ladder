class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        p = [[] for _ in range(len(graph))]
        q = [(0, [0])]
        ans = []
        while q:
            node, path = q.pop(0)
            if node == len(graph) - 1:
                ans.append(path)
            for c in graph[node]:
                q.append((c, path + [c]))
        return ans
