# Kth Smallest Element in a BST (Blind)

Given the `root` of a binary search tree, and an integer `k`, 
return the `kth` smallest value (**1-indexed**) of all the 
values of the nodes in the tree.


**Example 1**:

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

**Solution**:

Use inorder traversal (preferably using iteration)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            
            k -= 1
            
            if not k:
                return root.val
            root = root.right
```

Time Complexity: O(H+K) where H is the height of the tree

Space Complexity: O(H)