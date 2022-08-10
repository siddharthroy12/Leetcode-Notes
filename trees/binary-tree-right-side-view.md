# Binary Tree Right Side View

Given the `root` of a binary tree, imagine yourself standing on the *right side* of it, return the values of the nodes you can see ordered from top to bottom.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2**:

```
Input: root = [1,null,3]
Output: [1,3]
```

**Example 3**:

```
Input: root = []
Output: []
```

**Solution**:

Use BFS

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return  []
        
        current_level = [root]
        res = []
        
        while current_level:
            res.append(current_level[-1].val)
            
            new_level = []
            
            for node in current_level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
                
            current_level = new_level
            
        return res
```
