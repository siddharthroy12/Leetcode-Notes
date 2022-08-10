# Valid Sudoku

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` 
without repetition.

**Note**:
- A Sudoku board (partially filled) could be valid but is not necessarily 
solvable.
- Only the filled cells need to be validated according to the mentioned rules.

**Example 1**:

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
```
**Example 2**:

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since
there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Solution**:

```python
from math import floor

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            for y in range(9):
                num = board[x][y]
                
                if num != ".":
                    board[x][y] = "0"


                    # Check row
                    for xi in range(9):
                        if board[xi][y] == num:
                            return False

                    # Check columns
                    for yi in range(9):
                        if board[x][yi] == num:
                            return False

                    # Check 3x3 sub grid
                    grid_x = floor(x/3) * 3
                    grid_y = floor(y/3) * 3

                    for xi in range(grid_x, grid_x+3):
                        for yi in range(grid_y, grid_y+3):
                            if board[xi][yi] == num:
                                return False

                    board[x][y] = num
        return True
```