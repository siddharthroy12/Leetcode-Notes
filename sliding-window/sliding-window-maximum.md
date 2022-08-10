
# Sliding Window Maximum

You are given an array of integers `nums`, there is a sliding window of 
size `k` which is moving from the very left of the array to the very
right. You can only see the `k` numbers in the window. Each time the 
sliding window moves right by one position.

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

**Solution**

Use a deque and append the values in it as the window slides
maintain the decreasing order by popping the values from the back if they
are greater than the one you are going to append.

and the window slides check if the number in the front of the deque
is out of window if it is then pop it.

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # Will store numbers in decreasing order
        l = r = 0
        
        while r < len(nums):
            # Pop greater values than current right pointer
            # Before appending to right side
            # To maintain the decreasing ordera
            while len(q) and nums[q[-1]] < nums[r]:
                q.pop()
                
            q.append(r)
            
            # Pop the greatest number or the front number if it's out of window
            if l > q[0]:
                q.popleft()
            
            # Because thre window start with size zero
            # we need to check if the window has grown enough
            # to start sliding the left pointer
            # which we will use to check if the front of the deque
            # is out of window
            if (r + 1 >= k):
                l += 1
                res.append(nums[q[0]])
            
            r += 1
        
        return res
```

Time Complexity: O(n)

Space Complexity: O(n)
