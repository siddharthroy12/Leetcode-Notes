# Pacific Atlantic Water Flow

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        reach_pacific, reach_atlantic = set(), set()
        
        def dfs(r, c, visit, prev_height):
            if (r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                heights[r][c] < prev_height):
                return
            
            visit.add((r, c))
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            for nr, nc in directions:
                dfs(r+nr, c+nc, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, reach_pacific, heights[0][c])
            dfs(rows-1, c, reach_atlantic, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, reach_pacific, heights[r][0])
            dfs(r, cols-1, reach_atlantic, heights[r][cols-1])
        
        return reach_atlantic & reach_pacific
```