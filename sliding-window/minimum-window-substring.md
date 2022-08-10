# Minimum Window Substring

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the 
**minimum window substring** of s such that every character in `t` (**including 
duplicates**) is included in the window. If there is no such substring, return the 
empty string `""`.

The testcases will be generated such that the answer is **unique**.

A **substring** is a contiguous sequence of characters within the string.

**Example 1**:

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2**:

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3**:

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

**Solution**:

Start from window with size 1
increase the window from right until it includes k
shrink the window from left until it not includes k

save the size of window and left and right somewhere

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) :
            return ""
        window_frequency = {s[0]: 1}
        t_frequency = {}
        s_frequency = {}
        window_left = 0
        window_right = 0
        window_sizes = {}
        min_size = len(s)

        # Calculate s frequency
        for letter in s:
            if letter not in s_frequency:
                s_frequency[letter] = 1
            else:
                s_frequency[letter] += 1

        # Calculate t frequency
        for letter in t:
            if letter not in s_frequency:
                return ""
            if letter not in t_frequency:
                t_frequency[letter] = 1
            else:
                t_frequency[letter] += 1

        def t_in_window():
            for k, v in t_frequency.items():
                if k not in window_frequency or window_frequency[k] < v:
                    return False
            return True

        while True:
            # Increase window from front
            while (not t_in_window()) and (window_right < len(s) - 1):
                window_right += 1

                if s[window_right] not in window_frequency:
                    window_frequency[s[window_right]] = 1
                else:
                    window_frequency[s[window_right]] += 1

            # To get out of infinite loop
            if not t_in_window():
                break

            # Decrease window from back
            while t_in_window():
                window_frequency[s[window_left]] -= 1
                window_left += 1

                window_sizes[window_right - window_left + 2] = [window_left, window_right]
                min_size = min(min_size, window_right - window_left + 2)

        if min_size not in window_sizes:
            return ""
    
        res = ""
        for i in range(window_sizes[min_size][0]-1, window_sizes[min_size][1]+1):
            res += s[i]
        return res
```

Time Complexity: O(n)

Space Complexity: O(n)