class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s_idx, e_idx = j, j
                virtical = 0
                if matrix[i][j] == '1':
                    for k in range(j + 1, len(matrix[0])):
                        if matrix[i][k] == '0':
                            break
                        else:
                            e_idx = k
                            
                    for v in range(i - 1, -1, -1):
                        rec = True
                        if matrix[v][s_idx] == '1':
                            for r in range(s_idx, e_idx + 1):
                                if matrix[v][r] == '0':
                                    rec = False
                                    break
                            if rec:
                                virtical += 1
                        else:
                            break
                        if not rec:
                            break
                    for v in range(i, len(matrix)):
                        rec = True
                        if matrix[v][s_idx] == '1':
                            for r in range(s_idx, e_idx + 1):
                                if matrix[v][r] == '0':
                                    rec = False
                                    break
                            if rec:
                                virtical += 1
                        else:
                            break
                        if not rec:
                            break
                    ans = max(ans, (e_idx - s_idx + 1) * virtical)
                else:
                    continue
        return ans
