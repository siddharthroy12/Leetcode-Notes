# Subtree of Another Tree

Given the roots of two binary trees `root` and `subRoot`, 
return `true` if there is a subtree of `root` with the same 
structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of 
a node in `tree` and all of this node's descendants. The 
tree `tree` could also be considered as a subtree of itself.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)

```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)

```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        
        if not (root and subRoot):
            return False
        
        return ((self.isSubtree(root.left, subRoot)) or 
                (self.isSubtree(root.right, subRoot)) or
                (self.isSameTree(root, subRoot)))
    
    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 == None and tree2 == None:
            return True
        
        if not (tree1 and tree2):
            return False
        
        return ((tree1.val == tree2.val) and
                (self.isSameTree(tree1.left, tree2.left)) and 
                (self.isSameTree(tree1.right, tree2.right)))
```