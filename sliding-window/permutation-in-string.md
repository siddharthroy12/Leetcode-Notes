# Permutation in String

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, 
or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1**:

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2**:

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Solution**:

Use a sliding window of size s1 and check if it's the permutation of s1 at each step.

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        right = len(s1) - 1
        frequency_s1 = {}
        frequency_window = {}

        for letter in s1:
            if letter not in frequency_s1:
                frequency_s1[letter] = 1
            else:
                frequency_s1[letter] += 1

        for i in range(right+1):
            if s2[i] not in frequency_window:
                frequency_window[s2[i]] = 1
            else:
                frequency_window[s2[i]] += 1

        while frequency_s1 != frequency_window and right < len(s2) - 1:
            frequency_window[s2[left]] -= 1
            if frequency_window[s2[left]] == 0:
                del frequency_window[s2[left]]
            left += 1
            right += 1
            if s2[right] not in frequency_window:
                frequency_window[s2[right]] = 1
            else:
                frequency_window[s2[right]] += 1

        return frequency_s1 == frequency_window
```