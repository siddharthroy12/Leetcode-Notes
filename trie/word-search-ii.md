# Word Search II

Given an `m x n` board of characters and a list of strings 
words, return all `words` on the board.

Each word must be constructed from letters of sequentially 
**adjacent cells**, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be used 
more than once in a word.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)

```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

**Solution**:

Store all the words in a trie then use dfs on the trie and
the board and remove the word from the trie as you find them

```python
class TreeNode:
    def __init__(self):
        self.nexts = {}
        self.end = False
        
    def add_word(self, word):
        current = self
        for letter in word:
            if letter not in current.nexts:
                current.nexts[letter] = TreeNode()
            current = current.nexts[letter]
        current.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TreeNode()
        
        # Store all words in trie
        for word in words:
            root.add_word(word)
            
        rows, cols = len(board), len(board[0])
        
        res = []
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
               r == rows or c == cols or
               board[r][c] == None or board[r][c] not in node.nexts):
                return
            
            prev = node
            l = board[r][c]
            node = node.nexts[l]
            word += l
            
            if node.end:
                # Remove word from trie
                node.end = False
                if len(node.nexts) == 0:
                    del prev.nexts[l]
                    
                res.append(word)
            
            board[r][c] = None
            
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            
            board[r][c] = l
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
                
        return res
```