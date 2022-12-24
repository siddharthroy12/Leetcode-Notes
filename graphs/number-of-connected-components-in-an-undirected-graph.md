Use union find

```python
def solve(n, edges):
    par = [i for i in range(n)]
    rank [1] * n

    def root(n):
        res = n
        while res != par[res]:
            par[res] = par[par[res]] # Optional optimization
            res = par[res]
        return res

    def union(edge):
        root1 = root(edge[0])
        root2 = root(edge[1])

        if root1 == root2:
            return 0

        if rank[root1] > rank[root2]:
            rank[root1] += rank[root2]
            par[root2] = root1
        else:
            rank[root2] += rank[root1]
            par[root1] = root2

        return 1

    res = n
    for edge in edges:
        res -= union(edge)

    return res

```
