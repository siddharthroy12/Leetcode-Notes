# Binary Tree Level Order Traversal (Blind)

Given the `root` of a binary tree, return *the level order 
traversal of its nodes' values*. (i.e., from left to right, 
level by level).

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2**:

```
Input: root = [1]
Output: [[1]]
```

**Example 3**:

```
Input: root = []
Output: []
```

**Solution**:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return  []
        
        current_level = [root]
        res = []
        
        while current_level:
            res.append([node.val for node in current_level])
            new_level = []
            for node in current_level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            current_level = new_level
            
        return res
```