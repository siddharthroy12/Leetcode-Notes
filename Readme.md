# My Leetcode notes and solutions

These questions are taken from neetcode.io

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

### 1. Two Sum

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

Loop through each number, calculate target - number, the other pair(the result)
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
