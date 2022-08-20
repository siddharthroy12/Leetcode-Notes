### Top K Frequent Elements

Given an integer array nums and an integer `k`, return the `k` most frequent elements.
You may return the answer in any order.

**Example 1**:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2**:

```
Input: nums = [1], k = 1
Output: [1]
```

**Solution**:

First store the frequency of numbers in a hashmap where number is the key and
frequency is the value.
Then make a another hashmap where frequency is the key and the array of
numbers of the value.

We know that the largest frequency cannot be larger than the length of input array.
So finding the `k` most frequent elements from the second hashmap becomes easy.

```js
var topKFrequent = function(nums, k) {
    const counts = {};
    const countsSorted = {};
    const result = [];

    for (let num of nums) {
        if (counts[num] !== undefined) {
            counts[num]++;
        } else {
            counts[num] = 1;
        }
    }

    for (let key of Object.keys(counts)) {
        if (countsSorted[counts[key]]) {
            countsSorted[counts[key]].push(key);
        } else {
            countsSorted[counts[key]] = [key];
        }
    }

    let ik = 1;

    for (let i = nums.length; i > 0; i--) {
        if (ik > k) {
            break;
        }

        if (countsSorted[i] !== undefined) {
            for (let v of countsSorted[i]) {
                if (ik > k) {
                  break;
                }
                result.push(v);
                ik++;
            }
        }
    }

    return result;
};
```

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequencies; // number to frequency
        
        for (auto num : nums) {
            frequencies[num]++;
        }
        
        unordered_map<int, vector<int>> invFrequencies; // frequency to number
        
        for (auto pair : frequencies) {
            invFrequencies[pair.second].push_back(pair.first);
        }
        
        vector<int> res;
        
        for (int i = nums.size(); i > -1; i--) {
            if (invFrequencies.find(i) != invFrequencies.end()) {
                for (auto num : invFrequencies[i]) {
                    res.push_back(num);
                    
                    if (res.size() == k) {
                        break;
                    }
                }
            }
            
            if (res.size() == k) {
                break;
            }
        }
        
        return res;
    }
};
```

Time Complexity: O(n)

Space Complexity O(n)