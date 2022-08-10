# Largest Rectangle in Histogram

Given an array of integers `heights` representing the histogram's bar height 
where the width of each bar is `1`, return the area of the largest rectangle 
in the histogram.

***Example 1***:

![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

***Example 2***:

![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

```
Input: heights = [2,4]
Output: 4
```

**Solution**:

[Explaination](https://www.youtube.com/watch?v=zx5Sw9130L0)

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        
        stack = []
        
        for i, v in enumerate(heights):
            start = i
            
            while len(stack) and stack[-1][1] > v:
                index, height = stack.pop()
                largest_area = max(largest_area, height * (i - index))
                start = index
                
            stack.append([start, v])
        
        for i, h in stack:
            largest_area = max(largest_area, h * (len(heights) - i))

        return largest_area
```
