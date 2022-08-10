
# Search in Rotated Sorted Array (Blind)

There is an integer array `nums` sorted in ascending order (with *distinct* values).

Prior to being passed to your function, `nums` is *possibly rotated* at an unknown 
pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], 
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For 
example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]
`.

Given the array `nums` **after** the possible rotation and an integer `target`, return 
the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1**:

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2**:

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3**:

```
Input: nums = [1], target = 0
Output: -1
```

**Solution**

Just like a normal binary search but with some extra checks

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print(nums[mid])
            
            if nums[mid] == target:
                return mid
            
            # If on the left sorted side
            if nums[0] <= nums[mid]:
                if nums[mid] > target: # If mid is bigger than target
                    if target >= nums[left]: # if the target is in left side
                        right = mid - 1 # Move left side
                    else: # Move right side
                        left = mid + 1
                else: # if mid is smaller than target
                    left = mid + 1
                    
            else: # If on the right sorted side
                if nums[mid] > target: # If mid is bigger than target
                    right = mid - 1
                else: # If mid is smaller than target
                    if nums[right] >= target: # If target on the right side
                        left = mid + 1
                    else: # If target on the left side
                        right = mid - 1
                        
        return -1     
```