
# Longest Repeating Character Replacement

You are given a string `s` and an integer `k`. You can choose any
character of the string and change it to any other uppercase English character.
You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Example 1**:

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2**:

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

**Solution**:

Use a sliding window and keep expanding it. If the window is valid then calculate the longest.
If the window is not valid keep shrinking it unitl it is valid.

A window is valid if the `size of window - highest frequency in window <= k`.

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        seen = [0] * 27
        longest = 0

        # Sliding window in valid if the max frequency
        # minus the size of window is <= k
        def is_sliding_window_valid():
            highest = 0
            for i in range(ord("A"), ord("Z")+1):
                highest = max(highest, seen[i-65])
            if (right - left + 1) - highest <= k:
                return True
            return False

        while right < len(s):
            seen[ord(s[right])-65] += 1

            if is_sliding_window_valid():
                longest = max(longest, right - left)
            else: # If sliding window is not valid then shrink it until valid
                while not is_sliding_window_valid():
                    seen[ord(s[left])-65] -= 1
                    left += 1

            right += 1

        return longest + 1
```

Time Complexity O(n)

Space Complexity O(1)