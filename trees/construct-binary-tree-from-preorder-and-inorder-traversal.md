# Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays `preorder` and `inorder` where 
`preorder` is the preorder traversal of a binary tree and 
`inorder` is the inorder traversal of the same tree, 
construct and return the *binary tree*.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2**:

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

**Solution**

The first element of the preorder is the root node
and we can know which ones will go to left and right by 

finding the number in the inorder list, all the numbers on 
the left side will go in left side of the tree and all the 
numbers on the right side will go right side of the tree

if `mid` is the index of the root node in inorder
then the ``1 to `mid + 1` **(exclusive)** of preorder and 
`0` to `mid` **(exclusive)** of inorder will go to left 
and `mid + 1` to last of preorder and inorder will go to 
right

Do this recursively

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
```