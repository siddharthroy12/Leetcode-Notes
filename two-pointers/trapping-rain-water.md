# Trapping Rain Water

Given `n` non-negative integers representing an elevation map where the width of each bar is
`1`, compute how much water it can trap after raining.

**Example 1**:

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2**:

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Solution**:

To calculate how much water can be stored in each place you need to check the highest height
on the left and right side and get the minimum of that. Then minus it with the height of
current place.

```python
class Solution:
    def trap(self, height):
        water = [0] * len(height)

        highest_from_left = [0] * len(height)
        highest = 0
        
        # Calculate left highest for every palce
        for i, h in enumerate(height):
            if h > highest:
                highest = h
            highest_from_left[i] = highest

        highest_from_right = [0] * len(height)
        highest = 0
        
        # Calculate right highest for every palce
        for i, h in enumerate(reversed(height)):
            i = len(height) - 1 - i

            if h > highest:
                highest = h
            highest_from_right[i] = highest
        
        # Calculate height of water for every place
        # Calculate the min of left and right highest and minus current height from it
        for i, h in enumerate(height):
            min_ = min(highest_from_left[i], highest_from_right[i])
            if min_ > h:
                water[i] = min_-h
        
        # Count water
        total = 0
        for h in water:
            total += h

        return total
```

Time Complexity O(n)

Space Complexity O(n)

**Better Solution**:

We will use two pointer one on the left and one on the right.
And also keep track of the left highest and right heighest
check which one is the lowest of left and right highest
move the lowest one forward update the heightest and calculate the increase
in total

```python
class Solution:
    def trap(self, height):
        total = 0

        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                total += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                total += maxRight - height[right]
        return total
```

Time Complexity O(n)

Space Complexity O(1)
