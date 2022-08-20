# Group Anagrams

Given an array of strings `strs`, group the *anagrams* together.
You can return the answer in any order.

An **Anagram** is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

**Example 1**:

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2**:

```
Input: strs = [""]
Output: [[""]]
```

**Example 3**:

```
Input: strs = ["a"]
Output: [["a"]]
```

**Solution**:

We can store the groups in a hash map where the key will be an
array containing the counts of the letters by having the array size of 26
and the letter a is mapped to the first index of the array and letter z is the
last index of the array.

And the value of the hashmap will be a array of strings that belong to a single
anagram.

```js
var groupAnagrams = function(strs) {
    const res = {};

    for (let str of strs) {
        const count = new Array(26).fill(0);

        for (let letter of str) {
            const letterIndex = letter.charCodeAt(0) - "a".charCodeAt(0);

            count[letterIndex]++;
        }

        if (res[count]) {
            res[count].push(str);
        } else {
            res[count] = [str];
        }
    }

    return Object.values(res);
};
```

Using counting sort

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        
        for (auto str : strs) {
            string sorted = this->sortString(str);
            
            groups[sorted].push_back(str);
        }
        
        vector<vector<string>> res;
        
        for (auto pair : groups) {
            res.push_back(groups[pair.first]);
        }
        
        return res;
    }
    
    string sortString(string str) {
        int counts[26] = { 0 };
        
        for (auto letter : str) {
            counts[(int)letter - (int)'a'] += 1;
        }
        
        string res;
        
        for (char i = 0; i < 26; i++) {
            for (int j = 0; j < counts[i]; j++) {
                res.push_back(i + 'a');
            }
        }
        
        return res;
    }
};
```

Time Complexity: O(m * n) where n is the number of strings and m is
the average length of the string.

Space Complexity: O(n)