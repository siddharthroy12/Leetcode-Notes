# Rotting Oranges

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        fresh_oranges = 0
        rotten_oranges = 0
        
        coords_of_rotten_oranges = []
        
        # Get number of fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    rotten_oranges += 1
                    coords_of_rotten_oranges.append([r,c])
        
        if rotten_oranges == fresh_oranges == 0:
            return 0
        
        if rotten_oranges == 0:
            return -1
        
        if fresh_oranges == 0:
            return 0
        
        def bfs(start_level):
            seen = set()
            current_level = start_level
            
            for r, c in start_level:
                seen.add((r, c))
                
            time = -1
            rotted_oranges = 0
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            while current_level:
                time += 1
                new_level = []
                
                for cr, cc in current_level:
                    for dr, dc in directions:
                        nr = cr + dr
                        nc = cc + dc
                        if (nr in range(rows) and
                            nc in range(cols) and 
                            grid[nr][nc] == 1 and
                            (nr, nc) not in seen):
                            
                            rotted_oranges += 1
                            seen.add((nr, nc))
                            new_level.append([nr, nc])
                
                current_level = new_level
                
            return [rotted_oranges, time]
            
        rotted_oranges, time = bfs(coords_of_rotten_oranges)

        return time if rotted_oranges == fresh_oranges else -1
```