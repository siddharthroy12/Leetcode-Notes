# N-Queens

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the **n-queens puzzle**. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

**Example 2**:

```
Input: n = 1
Output: [["Q"]]
```

**Solution**:

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        pos_diag = set()
        neg_diag = set()
        
        board = []
        
        for i in range(n):
            board.append([])
            for j in range(n):
                board[-1].append(".")
        
        def recurse(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                
                board[r][c] = "Q"
                
                recurse(r+1)
                
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
                
        recurse(0)
        
        return res
                
```