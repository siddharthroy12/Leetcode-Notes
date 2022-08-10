# Two Sum II

Given a 1-indexed array of integers `numbers` that is already sorted in 
non-decreasing order, find two numbers such that they add up to a specific 
`target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` 
where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an 
integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may 
not** use the same element twice.

Your solution must use only constant extra space.

**Example 1**:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2**:

```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

**Example 3**:

```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

**Solution**:

Have two pointers pointing at the first and the last element of the array.

Calculate the sum, if the sum is bigger than target then that means you have to
move the last pointer towards left to decrease the sum and the exact opposite for
the first pointer.

Once the sum is equal to the target return the indexes with +1.

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0;
        right = len(numbers) - 1
        
        while (left < right):
            value = numbers[left] + numbers[right]
            
            if value == target:
                return [left+1, right+1]
            elif value > target:
                right -= 1
            else:
                left += 1
```