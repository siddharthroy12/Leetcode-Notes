# Serialize and Deserialize Binary Tree (Blind)

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

**Example 2**:

```
Input: root = []
Output: []
```

**Solution**:

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        def dfs(node) -> str:
            if not node:
                return "n"
            
            s = str(node.val) + ","
            
            s += dfs(node.left) + ","
            s += dfs(node.right)
            
            return s
    
        return dfs(root)
    
    def deserialize(self, data):
        l = data.split(",")
        
        i = 0
        
        def dfs():
            nonlocal i
            
            if l[i] == "n":
                i += 1
                return None
            
            node = TreeNode(int(l[i]))
            
            i += 1
            
            node.left = dfs()
            node.right = dfs()
        
            return node
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```