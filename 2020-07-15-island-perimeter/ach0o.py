class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        colsize = len(grid[0])
        rowsize = len(grid)

        total_peri = 0
        for ridx in range(rowsize):
            for cidx in range(colsize):
                if grid[ridx][cidx] != 1:
                    continue
                peri = 4
                if ridx - 1 >= 0:
                    if grid[ridx - 1][cidx] == 1:
                        peri -= 1
                if ridx + 1 < rowsize:
                    if grid[ridx + 1][cidx] == 1:
                        peri -= 1
                if cidx - 1 >= 0:
                    if grid[ridx][cidx - 1] == 1:
                        peri -= 1
                if cidx + 1 < colsize:
                    if grid[ridx][cidx + 1] == 1:
                        peri -= 1
                total_peri += peri
        return total_peri
