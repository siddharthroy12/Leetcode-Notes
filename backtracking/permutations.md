# Permutations

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

**Example 1**:

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2**:

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3**:

```
Input: nums = [1]
Output: [[1]]
```

**Solution**:

```python
class Solution:
    def solve(self, nums, results=[], progress=[], used={}):
        for num in nums:
            if not num in used or not used[num]:
                used[num] = True
                progress.append(num)
                self.solve(nums, results, progress, used)
                used[num] = False
                progress.pop()
        
        if len(nums) == len(progress):
            print(progress)
            results.append(progress.copy())
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.solve(nums, results)
        return results
```
