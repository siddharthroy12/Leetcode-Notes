# Word Search

Given an `m x n` grid of characters `board` and a string `word`,
return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

**Example 1**:

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2**:

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3**:

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

**Solution**:

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        
        def dfs(x, y, curIndex):
            if (((x,y) not in used) and
                (x >= 0) and
                (x < len(board)) and
                (y >= 0) and
                (y < len(board[0])) and
                (curIndex < len(word))):
            
                if board[x][y] == word[curIndex]:
                    if curIndex == len(word) - 1:
                        return True
                    
                    used.add((x,y))
                    
                    if dfs(x+1, y, curIndex+1): return True
                    if dfs(x-1, y, curIndex+1): return True
                    if dfs(x, y+1, curIndex+1): return True
                    if dfs(x, y-1, curIndex+1): return True
                    
                    used.remove((x, y))
                
            return False
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x, y, 0):
                    return True
        
        return False
```