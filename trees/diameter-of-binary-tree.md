# Diameter of Binary Tree

Given the `root` of a binary tree, return the length of the **diameter** of 
the tree.

The **diameter** of a binary tree is the **length** of the longest path 
between any two nodes in a tree. This path may or may not pass through the 
`root`.

The **length** of a path between two nodes is represented by the number of 
edges between them.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2**:

```
Input: root = [1,2]
Output: 1
```

**Solution**:

Count the left and right height for each nodes add them together and the highest diameter (left height + right height + 1) is the answer.


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        self.cache = {} # For memoization
        
        self.max_diameter = 0
        
        self.depthOfBinaryTree(root)
        
        return self.max_diameter - 1
        
    def depthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root in self.cache:
            return self.cache[root]
        
        if root == None:
            self.cache[root] = 0
            return 0
        
        lh = self.depthOfBinaryTree(root.left)
        rh = self.depthOfBinaryTree(root.right)
        
        self.max_diameter = max(self.max_diameter, lh+rh+1)
        
        h = max(lh, rh) + 1
        self.cache[root] = h
        
        return h

```