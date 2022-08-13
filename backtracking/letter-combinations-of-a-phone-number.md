# Letter Combinations of a Phone Number

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

**Example 1**:

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2**:

```
Input: digits = ""
Output: []
```

**Example 3**:

```
Input: digits = "2"
Output: ["a","b","c"]
```

**Solution**:

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        combinations = []
        
        mapping = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','v','u'],
            '9': ['w','x','y','z'],
        }
        
        current_combination = ""
        
        def dfs(i):
            nonlocal current_combination
            
            if len(current_combination) == len(digits):
                combinations.append(current_combination)
            
            if i == len(digits):
                return
            
            for letter in mapping[digits[i]]:
                current_combination += letter
                dfs(i+1)
                current_combination = current_combination[:-1]
                
        dfs(0)
        
        return combinations
```