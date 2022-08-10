# 3Sum

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` 
such that `i != j, i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1**:

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2**:

```
Input: nums = []
Output: []
```

**Example 3**:

```
Input: nums = [0]
Output: []
```

**Solution**:

Basically Two sum with a outer loop.

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i, num1 in enumerate(nums):
            seen = set() # Two sum starts here
            for j, num2 in enumerate(nums[i+1:]): # i + 1 Because i != j =! k
                num3 = -(num1+num2)
                if num3 in seen:
                    triplet = tuple(sorted([num1,num2,num3]))
                    # Saving in a hashset to avoid duplicates
                    triplets.add(triplet)
                else:
                    seen.add(num2)
        
        return triplets
```

Time Complexity O(n^2)

Space Complexity O(n)