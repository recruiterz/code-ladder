class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        if not matrix[0]:
            return False
        
        w = len(matrix[0])
        h = len(matrix)
        
        visited = [[False] * w for _h in range(h)]
        
        
        stack = [(0, 0)]
        
        while stack:
            _w, _h = stack.pop()
            visited[_h][_w] = True
            i = matrix[_h][_w]
            
            if target == i:
                return True
            
            if i < target:
                if _h + 1 < h and visited[_h + 1][_w] is False:
                    stack.append((_w, _h + 1))
                if _w + 1 < w and visited[_h][_w + 1] is False:
                    stack.append((_w + 1, _h))
            elif target < i:
                if 0 <= _h - 1 and visited[_h - 1][_w] is False:
                    stack.append((_w, _h - 1))
                if 0 <= _w - 1 and visited[_h][_w - 1] is False:
                    stack.append((_w - 1, _h))
        return False
        
