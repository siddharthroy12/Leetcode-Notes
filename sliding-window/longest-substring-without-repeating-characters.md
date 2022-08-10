# Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1**:

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2**:

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
**Example 3**:

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Solution**:

Use sliding window

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = right = 0
        seen = {}
        
        while right < len(s):
            if s[right] in seen:
                while s[right] in seen:
                    del seen[s[left]]
                    left += 1
            
            longest = max(longest, right - left + 1)
            
            seen[s[right]] = right
            right += 1
        
        return longest
                
```

Time Complexity: O(n)

Space Complexity: O(n)