# Clone Graph

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}
        
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            
            newNode = Node(node.val)
            hashmap[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            
            return newNode
        
        return dfs(node) if node else None
```