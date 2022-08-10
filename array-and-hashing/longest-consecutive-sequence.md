# Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

**Example1**:

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2**:

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Solution**:

First put all the numbers in a hashmap so we can access them in O(1).

Now for each number check if the `number - 1` exists if it doesn't then it's
the beginning of a sequence and then start counting the length of the sequence.

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            hashmap[num] = True

        starts = []

        for num in nums:
            if not num-1 in hashmap:
                starts.append(num)

        longest_length = 0

        for start in starts:
            length = 0
            while start in hashmap:
                start += 1
                length += 1

            if length > longest_length:
                longest_length = length

        return longest_length

```