# Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

You must solve it in `O(n)` time complexity.

**Example 1**:

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2**:

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Solution**:

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            if len(heap) == k+1:
                heapq.heappop(heap)
                
            heapq.heappush(heap, num)
        
        k_nums = []
        
        while heap:
            k_nums.append(heapq.heappop(heap))
 
        return k_nums[-k]
```

n log k is pretty close to n if k is smalls