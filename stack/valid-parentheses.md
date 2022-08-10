# Valid Parentheses (Blind)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}
'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example 1**:

```
Input: s = "()"
Output: true
```

**Example 2**:

```
Input: s = "()[]{}"
Output: true
```

**Example 3**:

```
Input: s = "(]"
Output: false
```

**Solution**:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingpairs = {')':'(', '}':'{', ']':'['}
        openingBrackets = set(["(", "{", "["])
        
        for letter in s:
            if letter in openingBrackets:
                stack.append(letter)
            elif len(stack):
                if letter in closingpairs and closingpairs[letter] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0
```

Time Complexity: O(n)
Space Complexity: O(n)
