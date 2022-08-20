# Walls and Gates

```python
from typing import (
    List,
)

INF = 2147483647

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        rows, cols = len(rooms), len(rooms[0])

        def bfs(start_level):
            visited = set()
            
            for r, c in start_level:
                visited.add((r, c))

            current_level = start_level

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            distance = 0

            while current_level:
                new_level = []
                distance += 1

                for r, c in current_level:
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if (nr in range(rows) and
                            nc in range(cols) and
                            rooms[nr][nc] == INF and
                            (nr, nc) not in visited):

                            rooms[nr][nc] = distance
                            visited.add((nr, nc))
                            new_level.append((nr, nc))

                current_level = new_level

        gates = []

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    gates.append([r, c])
        
        bfs(gates)
```