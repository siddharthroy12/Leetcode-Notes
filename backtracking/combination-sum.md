# Combination Sum

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

**Example 1**:

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2**:

```
Input: nums = [1], k = 1
Output: [1]
```

**Solution**:

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def permute(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            permute(i, cur, total+candidates[i])
            cur.pop()
            permute(i+1, cur, total)
        
        permute(0, [], 0)
        return res
```