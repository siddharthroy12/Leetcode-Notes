
# Daily Temperatures

Given an array of integers `temperatures` represents the daily 
temperatures, return an array `answer`    such that `answer[i]` is the 
number of days you have to wait after the `ith` day to get a warmer 
temperature. If there is no future day for which this is possible, keep 
`answer[i] == 0` instead.

**Example 1**:

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2**:

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3**:

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Solution**:

Use a monotinic decreasing stack

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # Decreasing stack
        
        # Add each value in the stack with index
        for i, v in enumerate(temperatures):
            # If the value we are adding is bigger than the
            # top one then we need to pop the values
            # until to top is not smaller than the one we are 
            # going to add to maintain the decreasing order
            # and as we are popping we can calculate value
            # for the index that we are popping
            while stack and stack[-1][1] < v:
                index, value = stack.pop()
                res[index] = i - index
                
            stack.append([i, v])
        
        return res
```

Time Complexity: O(n)

Space Complexity: O(n)