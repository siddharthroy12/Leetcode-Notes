# Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` 
respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Example 1**:

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2**:

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Solution**:

https://www.youtube.com/watch?v=q6IEA26hvXc

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        bigger_list = nums1
        smaller_list = nums2
        total_half = (len(nums1) + len(nums2)) // 2
        is_even = (len(bigger_list) + len(smaller_list)) % 2 == 0
        
        # Correct smaller and bigger list
        if len(smaller_list) > len(bigger_list):
            bigger_list, smaller_list = smaller_list, bigger_list
        
        # Binary search for left partition
        left = 0
        right = len(smaller_list) - 1
        
        while True:
            smaller_mid = (left + right) // 2
            bigger_mid = total_half - smaller_mid - 2
            
            smaller_left = smaller_list[smaller_mid] if smaller_mid >= 0 else float("-infinity")
            smaller_right = smaller_list[smaller_mid+1] if (smaller_mid + 1) < len(smaller_list) else float("infinity")
            bigger_left = bigger_list[bigger_mid] if bigger_mid >= 0 else float("-infinity")
            bigger_right = bigger_list[bigger_mid+1] if (bigger_mid + 1) < len(bigger_list) else float("infinity")
            
            if smaller_left <= bigger_right and bigger_left <= smaller_right:
                if is_even:
                    num1 = max(smaller_left, bigger_left)
                    num2 = min(smaller_right, bigger_right)
                    return (num1 + num2) / 2
                else:
                    return min(smaller_right, bigger_right)
            elif smaller_left > bigger_right:
                right = smaller_mid - 1
            else:
                left = smaller_mid + 1
```

Time Complexity: O(log min(num1, num2))