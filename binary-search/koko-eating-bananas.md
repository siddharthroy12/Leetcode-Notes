
# Koko Eating Bananas

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile 
has `piles[i]` bananas. The guards have gone and will come back in `h` 
hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she 
chooses some pile of bananas and eats `k` bananas from that pile. If the 
pile has less than `k` bananas, she eats all of them instead and will not 
eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas 
before the guards return.

Return the minimum integer `k` such that she can eat all the bananas 
within `h` hours.

**Example 1**:

```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

**Example 2**:

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

**Example 3**:

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

**Solution**:

The max eating speed is max(piles) and min eating speed is 1.

```python
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        
        def calculate_hour(speed):
            hour = 0
            
            for num in piles:
                hour += ceil(num/speed)
            
            return hour
        
        while left <= right:
            mid = (right+left) // 2

            if calculate_hour(mid) <= h:
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1
        
        return res
```

Time Complexity: O(log max(piles) * piles)

Space Complexity: O(1)