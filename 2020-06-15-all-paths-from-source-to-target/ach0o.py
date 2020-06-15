from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end_node = len(graph) - 1
        result = []

        # all paths start from node 0.
        que = deque()
        for adj in graph[0]:
            que.append([0, adj])

        while que:
            visited_nodes = que.popleft()

            if visited_nodes[-1] == end_node:
                # all paths ends at node (graph.length - 1)
                result.append(visited_nodes)
            else:
                latest_node = visited_nodes[-1]

                # enqueue adjacent nodes
                for _adj in graph[latest_node]:
                    if _adj > latest_node:  # paths should be ordered.
                        que.append(visited_nodes + [_adj])
        return result
