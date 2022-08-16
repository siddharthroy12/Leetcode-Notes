```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        max_area = 0
        
        def dfs(r, c):
            if (r in range(rows) and
                c in range(cols) and
                (r, c) not in visited and
                grid[r][c] == 1):
                
                visited.add((r, c))

                for dr, dc in directions:            
                    dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    size_before = len(visited)
                    dfs(r, c)
                    max_area = max(max_area, len(visited) - size_before)
                    islands += 1
        
        return max_area
```