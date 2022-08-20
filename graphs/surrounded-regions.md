# Surrounded Regions

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[0])
        
        def capture(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)
        
        # Capture unsurrounded regions (O -> T)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                    capture(r, c)
            
        # Capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Uncapture unsurrounded regions (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
```