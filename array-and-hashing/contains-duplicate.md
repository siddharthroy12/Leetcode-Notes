# Contains Duplicate

Given an integer array `nums`, return `true` if any value appears at least twice
in the array, and return `false` if every element is distinct.

**Example 1**:

```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2**:

```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3**:

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

**Solution**:

Just use a hashmap to store to seen numbers.

```js
var containsDuplicate = function(nums) {
    const seen = {};

    for (let num of nums) {
        if (seen[num]) {
            return true
        } else {
            seen[num] = true;
        }
    }

    return false;
}
```

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_map<int, bool> seen;
        
        for (auto num: nums) {
            if (seen.find(num) != seen.end()) {
                return true;
            } else {
                seen[num] = true;
            }
        }
        
        return false;
    }
};
```

Time Complexity: O(n)

Space Complexity O(n)