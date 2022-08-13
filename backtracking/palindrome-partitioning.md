# Palindrome Partitioning

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible **palindrome** partitioning of `s`.

A **palindrome** string is a string that reads the same backward as forward.

**Example 1**:

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

**Example 2**:

```
Input: s = "a"
Output: [["a"]]
```

**Solution**:

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        current_part = []
        
        def recurse(i):
            if i >= len(s):
                partitions.append(current_part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    current_part.append(s[i:j+1])
                    recurse(j+1)
                    current_part.pop()
            
        recurse(0)
        
        return partitions
        
    def isPalindrome(self, s: str) -> bool:
            alphanumeric_string = ""

            # Get Alphanumeric string
            for letter in s:
                ascii_value = ord(letter)

                # For numbers
                if ascii_value >= 48 and ascii_value <= 57:
                    alphanumeric_string += letter

                # For Uppercase letters
                elif ascii_value >= 65 and ascii_value <= 90:
                    alphanumeric_string += letter.lower()

                # For Lowercase letters
                elif ascii_value >= 97 and ascii_value <= 122:
                    alphanumeric_string += letter

            left = 0
            right = len(alphanumeric_string) - 1

            while (left < right):
                if alphanumeric_string[left] != alphanumeric_string[right]:
                    return False

                left += 1
                right -= 1

            return True
```