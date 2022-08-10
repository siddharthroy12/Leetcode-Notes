# Subsets

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1**:

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2**:

```
Input: nums = [0]
Output: [[],[0]]
```

**Solution**:

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        
        return res
```