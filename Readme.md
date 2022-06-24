# My Leetcode notes and solutions

These questions are taken from [neetcode.io](https://neetcode.io/)

The question maked as "blind" are from famous Blind 75 list.

## Table of Questions

1. [Array and Hasing](#array-and-hashing)
    1. [Contains Duplicate (Blind)](#217-contains-duplicate-blind)
    2. [Valid Anagram (Blind)](#242-valid-anagram-blind)
    3. [Two Sum (Blind)](#1-two-sum-blind)
    4. [Group Anagrams (Blind)](#49-group-anagrams-blind)
    5. [Top K Frequent Elements (Blind)](#347-top-k-frequent-elements-blind)
2. [Trie](#trie)
    1. [Implement Trie](#208-implement-trie-blind)
3. [Heap and Priority Queue](#heap-and-priority-queue)
    1. [Kth Largest Element in a Stream](#703-kth-largest-element-in-a-stream)
    2. [Last Stone Weight](#1046-last-stone-weight)

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

### 49. Group Anagrams (Blind)

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

Time Complexity: O(m * n) where n is the number of strings and m is
the average length of the string.

Space Complexity: O(n)

### 347. Top K Frequent Elements (Blind)

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

Time Complexity: O(n)

Space Complexity O(n)

## Trie

### 208. Implement Trie (Blind)

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in
the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously
inserted string `word` that has the prefix `prefix`, and `false` otherwise.

**Example 1**:

```
Input

["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output

[null, null, true, false, true, null, true]

Explanation

Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

**Solution**:

```js
class TrieNode {
  constructor(value) {
    this.value = value;
    this.nexts = {};
    this.end = false;
  }
}

var Trie = function() {
    this.root = new TrieNode(null);
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let currentNode = this.root;

  for (let i = 0; i < word.length; i++) {
    const letter = word[i];

    if (currentNode.nexts[letter]) {
      currentNode = currentNode.nexts[letter];

      if (i === word.length-1) {
        currentNode.end = true;
      }

      continue;
    } else {
      let newNode = new TrieNode(letter);

      currentNode.nexts[letter] = newNode;

      currentNode = newNode;

      if (i === word.length-1) {
        currentNode.end = true;
      }

      continue;
    }
  }
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let currentNode = this.root;

  for (let i = 0; i < word.length; i++) {
    const letter = word[i];

    if (!currentNode.nexts[letter]) {
      return true;
    }

    currentNode = currentNode.nexts[letter];
  }

  return currentNode.end;
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let currentNode = this.root;

  for (let i = 0; i < prefix.length; i++) {
    const letter = prefix[i];

    if (!currentNode.nexts[letter]) {
      return true;
    }

    currentNode = currentNode.nexts[letter];
  }

  return Object.keys(currentNode).length > 0;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```

Every method in this class has Time Complexity of O(n) where n is the
length of the input word.

## Heap and Priority Queue

### 703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is
the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

- `KthLargest(int k, int[] nums)` Initializes the object with the integer k
and the stream of integers nums.

- `int add(int val)` Appends the integer val to the stream and returns the
element representing the kth largest element in the stream.

**Example 1**:

```
Input

["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output

[null, 4, 5, 5, 8, 8]

Explanation

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

**Solution**:

The most naive approach to solve this problem is to just sort the array
using the built-in `sort` method when we first initialize the array.

Then finding the kth element would take `n` amount of time where `n` is the
size of the array. And adding an element to its correct
place will also take `n` amount of time.

But we can solve this problem with a better time complexity using a Heap.

And you may think that the max heap is the best solution for this because
inserting an element to a max heap takes log n time and we will always have
the biggest number at the top so finding kth element would take k amount of time.

So the overall time complexity of the `add` function will become O(k log n).

But if we use a min-heap we can make this even more time-efficient to
O(log k).

This is possible because we only want the kth element so if we will only store
the k largest element in a min-heap so we will have the kth largest number at
the top. And when we add a new number to the min-heap will we pop the smallest
number in the heap so the kth largest element will always be at the top.

I'm going to use Python for this because JavaScript doest not come
with Heap Data Structures.

The code:

```python
import heapq # Min heap implementation in python

class KthLargest:
  def __init__(self, k: int, nums: List[int]): # O(log n + n) = O(log n)
    self.min_heap, self.k = nums, k

    heapq.heapify(self.min_heap) # O(log n)

    # Removing numbers that are not k largest O(n)
    while len(self.min_heap) > self.k:
      heapq.heappop(self.min_heap)

  def add(self, val: int) -> int: # O(log k + log k) = O(log k)
    heapq.heappush(self.min_heap, val) # Add new number O(log k)

    # Pop minimum number if the size of heap is bigger than k
    if len(self.min_heap) > self.k:
      heapq.heappop(self.min_heap) # O(log k)

    return self.min_heap[0]
```

### 1046. Last Stone Weight

You are given an array of integers `stones` where `stones[i]` is the weight of
the ith stone.

We are playing a game with the stones. On each turn,
we choose the **heaviest two stones** and smash them together.
Suppose the heaviest two stones have weights `x` and `y` with `x <= y`.

The result of this smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y`
has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return the weight of the last remaining stone.
If there are no stones left, return `0`.

**Example 1**:

```
Input: stones = [2,7,4,1,8,1]

Output: 1

Explanation: 

We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's
the value of the last stone.
```

```
Example 2:

Input: stones = [1]

Output: 1
```

**Solution**:

Since Python doesn't have a max heap we'll store all the
numbers as negative and convert them to positive when we need it.

Other than that, everything is explained well in the
question what we have to do.

```python
class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    self.max_heap = []

    # Storing the weights as negative
    # Because heapq is a min heap
    for stone in stones:
      heapq.heappush(self.max_heap, -stone)

    while len(self.max_heap) > 1:
      first = heapq.heappop(self.max_heap)
      second = heapq.heappop(self.max_heap)

      if first != second:
        new_stone = first - second
        heapq.heappush(self.max_heap, new_stone)

    if len(self.max_heap) == 0:
      return 0

    return -self.max_heap[0]
```

Time Complexity: O(n log n)

Space Complexity O(n)

