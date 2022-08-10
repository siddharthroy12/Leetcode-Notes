# Valid Palindrome

A phrase is a **palindrome** if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the same 
forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Example 1**:

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2**:

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3**:

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Solution**:

```python
class Solution:
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
