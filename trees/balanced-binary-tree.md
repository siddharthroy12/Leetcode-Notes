# Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

>a binary tree in which the left and right subtrees of every node differ in 
>height by no more than 1.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3**:

```
Input: root = []
Output: true
```

**Solution**:

Use dfs and check the lowest one first 

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root: Optional[TreeNode]) -> [bool, int]:
            if not root:
                return [True, 0]
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            balanced = (l[0] and r[0] and 
                        abs(l[1] - r[1]) <= 1)
            
            return [balanced, max(l[1], r[1]) + 1]
        
        return dfs(root)[0]
```