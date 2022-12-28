```python
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n, edges):
        # For dumb edge cases
        if n == 0:
            return False
        if len(edges) != n-1:
            return False
        # write your code here
        parents = [i for i in range(n)]
        rank = [0] * n

        def find(n):
            p = parents[n]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(edge):
            x_parent = find(edge[0])
            y_parent = find(edge[1])

            if x_parent == y_parent:
                return True
            else:
                if rank[x_parent] > rank[y_parent]:
                    parents[x_parent] = y_parent
                    rank[x_parent] += 1
                else:
                    parents[y_parent] = x_parent
                    rank[y_parent] += 1
            return False

        for edge in edges:
            if union(edge):
                return False

        return True
```
