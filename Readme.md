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
    6. [Product of Array Except Self (Blind)](#238-product-of-array-except-self-blind)
    7. [Valid Sudoku](#36-valid-sudoku)
    8. [Encode and Decode Strings (Blind)](#271-encode-and-decode-strings-blind)
    9. [Longest Consecutive Sequence (Blind)](#128-longest-consecutive-sequence-blind)
2. [Two Pointers](#two-pointers)
    1. [Valid Palindrome (Blind)](#125-valid-palindrome-blind)
    2. [Two Sum II](#167-two-sum-ii)
    3. [3Sum (Blind)](#15-3sum-blind)
    4. [Container With Most Water (Blind)](#11-container-with-most-water-blind)
3. [Trie](#trie)
    1. [Implement Trie (Blind)](#208-implement-trie-blind)
4. [Heap and Priority Queue](#heap-and-priority-queue)
    1. [Kth Largest Element in a Stream](#703-kth-largest-element-in-a-stream)
    2. [Last Stone Weight](#1046-last-stone-weight)
5. [Backtracking](#backtracking)
    1. [Permutations](#46-permutations)
    2. [Sudoku Solver](#37-sudoku-solver)

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

### 238. Product of Array Except Self (Blind)

Given an integer array `nums`, return an array `answer` such that `answer[i]`
is equal to the product of all the elements of nums except `nums[i]`.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

**Example 1**:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

**Example 2**:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

**Solution**:

We need to create two arrays with the length of input.

In one array each element is equal the the product of all element in
it's left side of input.

Do one for the right side too.

Now create the `result` array and for each element you just need to multiply
the left side of left array and right side of right array.

```python
class Solution:
    def productExceptSelf(self, nums):
        left_products = [None] * len(nums)
        right_products = [None] * len(nums)
        answer = []

        previous_product = 1

        for i in range(0, len(nums)):
            product = previous_product * nums[i]
            left_products[i] = product
            previous_product = product

        previous_product = 1

        for i in reversed(range(len(nums))):
            product = previous_product * nums[i]
            right_products[i] = product
            previous_product = product

        for i in range(len(nums)):
            current_product = 1

            if i > 0:
                current_product = current_product * left_products[i-1]

            if i < len(nums)- 1:
                current_product = current_product * right_products[i+1]

            answer.append(current_product)

        return answer
```

### 36. Valid Sudoku

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` 
without repetition.

**Note**:
- A Sudoku board (partially filled) could be valid but is not necessarily 
solvable.
- Only the filled cells need to be validated according to the mentioned rules.

**Example 1**:

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
```
**Example 2**:

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since
there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Solution**:

```python
from math import floor

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            for y in range(9):
                num = board[x][y]
                
                if num != ".":
                    board[x][y] = "0"


                    # Check row
                    for xi in range(9):
                        if board[xi][y] == num:
                            return False

                    # Check columns
                    for yi in range(9):
                        if board[x][yi] == num:
                            return False

                    # Check 3x3 sub grid
                    grid_x = floor(x/3) * 3
                    grid_y = floor(y/3) * 3

                    for xi in range(grid_x, grid_x+3):
                        for yi in range(grid_y, grid_y+3):
                            if board[xi][yi] == num:
                                return False

                    board[x][y] = num
        return True
```

### 271. Encode and Decode Strings (Blind)

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

### 128. Longest Consecutive Sequence (Blind)

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

**Example1**:

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2**:

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Solution**:

First put all the numbers in a hashmap so we can access them in O(1).

Now for each number check if the `number - 1` exists if it doesn't then it's
the beginning of a sequence and then start counting the length of the sequence.

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            hashmap[num] = True

        starts = []

        for num in nums:
            if not num-1 in hashmap:
                starts.append(num)

        longest_length = 0

        for start in starts:
            length = 0
            while start in hashmap:
                start += 1
                length += 1

            if length > longest_length:
                longest_length = length

        return longest_length

```
## Two Pointers

### 125. Valid Palindrome (Blind)

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

### 167. Two Sum II

Given a 1-indexed array of integers `numbers` that is already sorted in 
non-decreasing order, find two numbers such that they add up to a specific 
`target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` 
where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an 
integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may 
not** use the same element twice.

Your solution must use only constant extra space.

**Example 1**:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2**:

```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

**Example 3**:

```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

**Solution**:

Have two pointers pointing at the first and the last element of the array.

Calculate the sum, if the sum is bigger than target then that means you have to
move the last pointer towards left to decrease the sum and the exact opposite for
the first pointer.

Once the sum is equal to the target return the indexes with +1.

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0;
        right = len(numbers) - 1
        
        while (left < right):
            value = numbers[left] + numbers[right]
            
            if value == target:
                return [left+1, right+1]
            elif value > target:
                right -= 1
            else:
                left += 1
```

### 15. 3Sum (Blind)

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` 
such that `i != j, i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1**:

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2**:

```
Input: nums = []
Output: []
```

**Example 3**:

```
Input: nums = [0]
Output: []
```

**Solution**:

Basically Two sum with a outer loop.

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i, num1 in enumerate(nums):
            seen = set() # Two sum starts here
            for j, num2 in enumerate(nums[i+1:]): # i + 1 Because i != j =! k
                num3 = -(num1+num2)
                if num3 in seen:
                    triplet = tuple(sorted([num1,num2,num3]))
                    # Saving in a hashset to avoid duplicates
                    triplets.add(triplet)
                else:
                    seen.add(num2)
        
        return triplets
```

Time Complexity O(n^2)

Space Complexity O(n)

### 11. Container With Most Water (Blind)

You are given an integer array `height` of length `n`. There are `n` vertical 
lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.

**Example 1**:

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2**:

```
Input: height = [1,1]
Output: 1
```

**Solution**:

Use two pointers left and right calculate area and move the pointer with the shortest length
towards other side.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        
        max_area = 0
        
        while left < right:
            left_height, right_height = height[left], height[right]
            minheight = min(left_height, right_height)
            area = minheight * (right - left)

            
            if area > max_area:
                max_area = area
            
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_area
```

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
      return false;
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
      return false;
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

## Backtracking

### 46. Permutations

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

**Example 1**:

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2**:

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3**:

```
Input: nums = [1]
Output: [[1]]
```

**Solution**:

```pyhton
class Solution:
    def solve(self, nums, results=[], progress=[], used={}):
        for num in nums:
            if not num in used or not used[num]:
                used[num] = True
                progress.append(num)
                self.solve(nums, results, progress, used)
                used[num] = False
                progress.pop()
        
        if len(nums) == len(progress):
            print(progress)
            results.append(progress.copy())
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.solve(nums, results)
        return results
```

### 37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3`
sub-boxes of the grid.

The `'.'` character indicates empty cells.

**Example 1**:

```
Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]

Explanation: The input board is shown above and the only valid solution is shown below:
```

**Solution**:

```python
class Solution:
    def getValidNumbers(self, board, x, y):
        validNumbers = {}
        
        for i in range(1, 10):
            validNumbers[str(i)] = True
        
        # Row
        for xi in range(len(board)):
            validNumbers[board[xi][y]] = False
        
        # Columns
        for yi in range(len(board)):
            validNumbers[board[x][yi]] = False
            
        # 3x3 grid
        gridX = floor(x/3) * 3
        gridY = floor(y/3) * 3
        
        for xi in range(gridX, gridX+3):
            for yi in range(gridY, gridY+3):
                validNumbers[board[xi][yi]] = False
                
        results = []
        
        for i in range(1, 10):
            if validNumbers[str(i)]:
                results.append(str(i))
        
        return results
    
    def solveSudoku(self, board):
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == ".":
                    validNumbers = self.getValidNumbers(board, x, y)
                    
                    for number in validNumbers:
                        board[x][y] = number

                        
                        res = self.solveSudoku(board)
                        
                        if not res:
                            board[x][y] = "."
                            continue
                        else:
                            return True
        
                    return False
        return True

```