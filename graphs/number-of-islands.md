# Number of Islands

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1**:

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Output: 1
```

**Example 2**:

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def dfs(r, c):
            if (r in range(rows) and
                c in range(cols) and
                (r, c) not in visited and
                grid[r][c] == "1"):
                
                visited.add((r, c))

                for dr, dc in directions:            
                    dfs(r+dr, c+dc)
                
        def bfs(r, c):
            blocks = [(r, c)]

            while len(blocks) != 0:
                new_blocks = []
                
                for block in blocks:
                    visited.add(block)
                    
                    for dr, dc in directions:
                        new_block = (block[0]+dr, block[1]+dc)
                        
                        if (new_block not in visited and
                            new_block[0] in range(rows) and
                            new_block[1] in range(cols) and
                            grid[new_block[0]][new_block[1]] == "1"):
                            new_blocks.append(new_block) 
                
                blocks = new_blocks
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        
        return islands
```