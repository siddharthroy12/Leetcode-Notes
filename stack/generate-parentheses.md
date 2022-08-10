
# Generate Parentheses

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1**:

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2**:

```
Input: n = 1
Output: ["()"]
```

**Solution**:

Use recursion and backtracking

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(s, o, c):
            if o == c and c == n:
                res.append(s)

            # If we can open more
            if o < n:
                recurse(s+"(", o+1, c)

            # If we can close
            if c < o:
                recurse(s+")", o, c+1)

        recurse("", 0, 0)

        return res
```