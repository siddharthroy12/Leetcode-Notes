# 684. Redundant Connection

Use Union find

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]
        rank = [1 for _ in range(len(edges)+1)]

        # Find the parent of parent of parent until the parent has not parent
        def find(n):
            p = parents[n]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        # Let's see if the greatest grand parents of the
        # two points of this edge is same or not
        def union(edge):
            x_parent = find(edge[0])
            y_parent = find(edge[1])

            if x_parent == y_parent:
                return False
            else:
                if rank[x_parent] > rank[y_parent]:
                    parents[x_parent] = y_parent
                    rank[x_parent] += 1
                else:
                    parents[y_parent] = x_parent
                    rank[y_parent] += 1
            return True

        for edge in edges:
            if not union(edge):
                return edge
```
