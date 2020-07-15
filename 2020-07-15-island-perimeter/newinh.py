class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        height = len(grid)
        width = len(grid[0])
    
        def is_island(h, w) -> bool:
            return grid[h][w] == 1
        
        
        def count_border(h, w) -> int:
            nn = int(h == 0 or grid[h-1][w] == 0)
            ss = int(h == height -1 or grid[h+1][w] == 0)
            ww = int(w == 0 or grid[h][w-1] == 0)
            ee = int(w == width - 1 or grid[h][w+1] == 0)
            return nn + ss + ww + ee
        
        perimeter = 0
        for _h in range(height):
            for _w in range(width):
                if is_island(_h, _w):
                    perimeter += count_border(_h, _w)
        return perimeter
