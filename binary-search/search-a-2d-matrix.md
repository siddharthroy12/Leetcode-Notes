# Search a 2D Matrix

Write an efficient algorithm that searches for a value `target` in an `m x 
n` integer matrix matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the 
previous row.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

**Solution**:

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        
        def flat_to_mat(i):
            return (i//width, i - ((i//width) * width))
        
        left = 0
        right = (width * height) - 1
        
        while left <= right:
            mid = (left+right) // 2
            x, y = flat_to_mat(mid)
            
            if matrix[x][y] > target:
                right = mid - 1
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                return True
        
        return False
```

Time Comlexity: O(log n)

Space Complexity: O(1)
