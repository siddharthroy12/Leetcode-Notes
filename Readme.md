# My Leetcode notes and solutions

These questions are taken from [neetcode.io](https://neetcode.io/)

The question maked as "blind" are from famous Blind 75 list.

## Array and Hashing

### 217. Contains Duplicate (Blind)

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

Time Complexity: O(n)

Space Complexity O(n)

### 242. Valid Anagram (Blind)

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

### 1. Two Sum (Blind)

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

**Example 1**:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2**:

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3**:

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Solution**:

Create a hashmap to store seen numbers with it's index.

Loop through each number, calculate target - number, if the other pair(the result)
exists inside the hashmap then just return the two indexes.

If the other pair does not exist store the current number in the hashmap.

```js
var twoSum = function(nums, target) {
    const seen = {};

    for (let i = 0; i < nums.length; i++) {
        const otherPair = target - nums[i];

        if (seen[otherPair] != undefined) {
            return [i, seen[otherPair]];
        } else {
            seen[nums[i]] = i;
        }
    }
};
```

Time Complexity: O(n)

Space Complexity O(n)

### 49. Group Anagrams

Given an array of strings `strs`, group the *anagrams* together.
You can return the answer in any order.

An *Anagram* is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

*Example 1*:

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

*Example 2*:

```
Input: strs = [""]
Output: [[""]]
```

*Example 3*:

```
Input: strs = ["a"]
Output: [["a"]]
```

*Solution*:

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

Time Complexity: O(m * n) where n is the number of strings and m is
the average length of the string.

Space Complexity: O(n)

### 347. Top K Frequent Elements

Given an integer array nums and an integer `k`, return the `k` most frequent elements.
You may return the answer in any order.

*Example 1*:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

*Example 2*:

```
Input: nums = [1], k = 1
Output: [1]
```

*Solution*:

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

Time Complexity: Maybe O(n)
Space Complexity Maybe O(n)
