# Subsets II

Given an integer array `nums` that may contain duplicates, return *all possible subsets (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in any **order**.

**Example 1:**

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]
```

**Solution:**

Do the same as subsets but first sort the input and when you choose to add the next one
skip all the dups.

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        
        return res
```