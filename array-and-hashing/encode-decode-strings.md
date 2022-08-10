# Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is 
then sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode`

**Example1**:

```
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
```

**Example2**:

```
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
```

**Solution**:

```python
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        result = ""

        for word in list:
            for letter in word:
                if letter == "$":
                    result += "/$"
                elif letter == "/":
                    result += "//"
                else:
                    result += letter
            result += "$"

        return result


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        result = []
        current_word = ""

        i = 0

        while i < len(string):
            letter = string[i]

            if letter == "$":
                result.append(current_word)
                current_word = ""
            elif letter == "/":
                if string[i+1] == "$":
                    current_word += "$"
                    i += 1
                elif string[i+1] == "/":
                    current_word += "/"
                    i += 1
            else:
                current_word += letter

            i += 1

        return result
```
