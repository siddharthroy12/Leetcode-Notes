# Valid Anagram

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and
`false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

**Example 1**:

```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2**:

```
Input: s = "rat", t = "car"
Output: false
```

**Solution**:

First loop through the first string and count how many times letters occur and store
it in a hashmap.

Then loop through the second string and check if the letter exists in the hashmap.
If exists decrease the count by 1, If does not exist then return false.

Finally loop through the values of hashmap. If any value is not 0 then return false

At the end return true.

```js
var isAnagram = function(s, t) {
    let count = {};

    for (let letter of s) {
        if (count[letter] >= 0) {
            count[letter]++;
        } else {
            count[letter] = 1;
        }
    }

    for (let letter of t) {
        if (count[letter] >= 0) {
            count[letter]--;
        } else {
            return false
        }
    }

    for (let letter of Object.keys(count)) {
        if (count[letter] != 0) {
            return false
        }
    }

    return true;
};
```

Time complexity: O(a+b)

Space complexity O(M) where m is the size of different letters