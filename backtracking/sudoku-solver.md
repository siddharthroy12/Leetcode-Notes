# Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3`
sub-boxes of the grid.

The `'.'` character indicates empty cells.

**Example 1**:

```
Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]

Explanation: The input board is shown above and the only valid solution is shown below:
```

**Solution**:

```python
class Solution:
    def getValidNumbers(self, board, x, y):
        validNumbers = {}

        for i in range(1, 10):
            validNumbers[str(i)] = True

        # Row
        for xi in range(len(board)):
            validNumbers[board[xi][y]] = False

        # Columns
        for yi in range(len(board)):
            validNumbers[board[x][yi]] = False

        # 3x3 grid
        gridX = floor(x/3) * 3
        gridY = floor(y/3) * 3

        for xi in range(gridX, gridX+3):
            for yi in range(gridY, gridY+3):
                validNumbers[board[xi][yi]] = False

        results = []

        for i in range(1, 10):
            if validNumbers[str(i)]:
                results.append(str(i))

        return results

    def solveSudoku(self, board):
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == ".":
                    validNumbers = self.getValidNumbers(board, x, y)

                    for number in validNumbers:
                        board[x][y] = number


                        res = self.solveSudoku(board)

                        if not res:
                            board[x][y] = "."
                            continue
                        else:
                            return True

                    return False
        return True

```