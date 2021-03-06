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
    5. [Trapping Rain Water](#42-trapping-rain-water)
3. [Sliding Window](#sliding-window)
    1. [Best Time to Buy and Sell Stock (Blind)](#121-best-time-to-buy-and-sell-stock-blind)
    2. [Longest Substring Without Repeating Characters (Blind)](#3-longest-substring-without-repeating-characters-blind)
    3. [Longest Repeating Character Replacement (Blind)](#424-longest-repeating-character-replacement-blind)
    4. [Permutation in String](#567-permutation-in-string)
    5. [Minimum Window Substring (Blind)](#76-minimum-window-substring-blind)
    6. [Sliding Window Maximum](#239-sliding-window-maximum)
4. [Stack](#stack)
    1. [Valid Parentheses (Blind)](#20-valid-parentheses-blind)
    2. [Min Stack](#155-min-stack)
    3. [Evaluate Reverse Polish Notation](#150-evaluate-reverse-polish-notation)
    4. [Generate Parentheses](#22-generate-parentheses)
    5. [Daily Temperatures](#739-daily-temperatures)
    6. [Car Fleet](#853-car-fleet)
    7. [Largest Rectangle in Histogram](#84-largest-rectangle-in-histogram)
5. [Binary Search](#binary-search)
    1. [Binary Search](#704-binary-search)
    2. [Search a 2D Matrix](#74-search-a-2d-matrix)
    3. [Koko Eating Bananas](#875-koko-eating-bananas)
    4. [Search in Rotated Sorted Array (Blind)](#33-search-in-rotated-sorted-array-blind)
    5. [Find Minimum in Rotated Sorted Array (Blind)](#153-find-minimum-in-rotated-sorted-array-blind)
    6. [Time Based Key-Value Store](#981-time-based-key-value-store)
    7. [Median of Two Sorted Arrays](#4-median-of-two-sorted-arrays)
6. [Linked List](#linked-list)
    1. [Reverse Linked List (Blind)](#206-reverse-linked-list-blind)
    2. [Merge Two Sorted Lists (Blind)](#21-merge-two-sorted-lists-blind)
    3. [Reorder List (Blind)](#143-reorder-list-blind)
    4. [Remove Nth Node From End of List (Blind)](#19-remove-nth-node-from-end-of-list-blind)
    5. [Copy List with Random Pointer](#138-copy-list-with-random-pointer)
    6. [Add Two Numbers](#2-add-two-numbers)
    7. [Linked List Cycle (Blind)](#141-linked-list-cycle-blind)
    8. [Find the Duplicate Number](#287-find-the-duplicate-number)
    9. [LRU Cache](#146-lru-cache)
    10. [Merge k Sorted Lists (Blind)](#23-merge-k-sorted-lists-blind)
    11. [Reverse Nodes in k-Group](#25-reverse-nodes-in-k-group)
7. [Trees](#trees)
    1. [Invert Binary Tree (Blind)](#226-invert-binary-tree-blind)
    2. [Maximum Depth of Binary Tree (Blind)](#104-maximum-depth-of-binary-tree-blind)
    3. [Diameter of Binary Tree](#543-diameter-of-binary-tree)
    4. [Balanced Binary Tree](#110-balanced-binary-tree)
    5. [Same Tree (Blind)](#100-same-tree-blind)
    6. [Subtree of Another Tree (Blind)](#572-subtree-of-another-tree-blind)
    7. [Lowest Common Ancestor of a Binary Search Tree (Blind)](#235-lowest-common-ancestor-of-a-binary-search-tree-blind)
    8. [Binary Tree Level Order Traversal (Blind)](#102-binary-tree-level-order-traversal-blind)
    9. [Binary Tree Right Side View](#199-binary-tree-right-side-view)
    10. [Count Good Nodes in Binary Tree](#1448-count-good-nodes-in-binary-tree)
    11. [Validate Binary Search Tree (Blind)](#98-validate-binary-search-tree-blind)
    12. [Kth Smallest Element in a BST (Blind)](#230-kth-smallest-element-in-a-bst-blind)
    12. [Construct Binary Tree from Preorder and Inorder Traversal (Blind)](#105-construct-binary-tree-from-preorder-and-inorder-traversal-blind)
    13. [Binary Tree Maximum Path Sum (Blind)](#124-binary-tree-maximum-path-sum-blind)
    14. [Serialize and Deserialize Binary Tree (Blind)](#297-serialize-and-deserialize-binary-tree-blind)
8. [Trie](#trie)
    1. [Implement Trie (Blind)](#208-implement-trie-blind)
    2. [Design Add and Search Words Data Structure (Blind)](#211-design-add-and-search-words-data-structure-blind)
    3. [Word Search II (Blind)](#212-word-search-ii-blind)
9. [Heap and Priority Queue](#heap-and-priority-queue)
    1. [Kth Largest Element in a Stream](#703-kth-largest-element-in-a-stream)
    2. [Last Stone Weight](#1046-last-stone-weight)
    3. [K Closest Points to Origin](#973-k-closest-points-to-origin)
    4. [Kth Largest Element in an Array](#215-kth-largest-element-in-an-array)
    5. [Task Scheduler](#621-task-scheduler)
    6. [Design Twitter](#355-design-twitter)
    7. [Find Median from Data Stream (Blind)](#295-find-median-from-data-stream-blind)
10. [Backtracking](#backtracking)
    1. [Permutations](#46-permutations)
    2. [Sudoku Solver](#37-sudoku-solver)
    3. [Subsets](#78-subsets)

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

### 42. Trapping Rain Water

Given `n` non-negative integers representing an elevation map where the width of each bar is
`1`, compute how much water it can trap after raining.

**Example 1**:

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2**:

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Solution**:

To calculate how much water can be stored in each place you need to check the highest height
on the left and right side and get the minimum of that. Then minus it with the height of
current place.

```python
class Solution:
    def trap(self, height):
        water = [0] * len(height)

        highest_from_left = [0] * len(height)
        highest = 0
        
        # Calculate left highest for every palce
        for i, h in enumerate(height):
            if h > highest:
                highest = h
            highest_from_left[i] = highest

        highest_from_right = [0] * len(height)
        highest = 0
        
        # Calculate right highest for every palce
        for i, h in enumerate(reversed(height)):
            i = len(height) - 1 - i

            if h > highest:
                highest = h
            highest_from_right[i] = highest
        
        # Calculate height of water for every place
        # Calculate the min of left and right highest and minus current height from it
        for i, h in enumerate(height):
            min_ = min(highest_from_left[i], highest_from_right[i])
            if min_ > h:
                water[i] = min_-h
        
        # Count water
        total = 0
        for h in water:
            total += h

        return total
```

Time Complexity O(n)

Space Complexity O(n)

**Better Solution**:

We will use two pointer one on the left and one on the right.
And also keep track of the left highest and right heighest
check which one is the lowest of left and right highest
move the lowest one forward update the heightest and calculate the increase
in total

```python
class Solution:
    def trap(self, height):
        total = 0

        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                total += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                total += maxRight - height[right]
        return total
```

Time Complexity O(n)

Space Complexity O(1)

## Sliding Window

### 121. Best Time to Buy and Sell Stock (Blind)

You are given an array `prices` where `prices[i]` is the price of a given stock on 
the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and 
choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot 
achieve any profit, return `0`.

**Example 1**:

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2**:

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

**Solution**:

Have two pointers one is the for buying and another for selling.
Initially buying pointer will point at the first and selling pointer will point at
second.

Calculate the profit and store the max profit in a variable if the proft is negative then
move the buying pointer to the selling pointer and move the selling pointer to next.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        left = 0
        right = 1
        
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                profit = prices[right] - prices[left]
                
                max_profit = max(max_profit, profit)
                right += 1
        
        return max_profit
```

### 3. Longest Substring Without Repeating Characters (Blind)

Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1**:

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2**:

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
**Example 3**:

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Solution**:

Use sliding window

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = right = 0
        seen = {}
        
        while right < len(s):
            if s[right] in seen:
                while s[right] in seen:
                    del seen[s[left]]
                    left += 1
            
            longest = max(longest, right - left + 1)
            
            seen[s[right]] = right
            right += 1
        
        return longest
                
```

Time Complexity: O(n)

Space Complexity: O(n)

### 424. Longest Repeating Character Replacement (Blind)

You are given a string `s` and an integer `k`. You can choose any
character of the string and change it to any other uppercase English character.
You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Example 1**:

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2**:

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

**Solution**:

Use a sliding window and keep expanding it. If the window is valid then calculate the longest.
If the window is not valid keep shrinking it unitl it is valid.

A window is valid if the `size of window - highest frequency in window <= k`.

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        seen = [0] * 27
        longest = 0

        # Sliding window in valid if the max frequency
        # minus the size of window is <= k
        def is_sliding_window_valid():
            highest = 0
            for i in range(ord("A"), ord("Z")+1):
                highest = max(highest, seen[i-65])
            if (right - left + 1) - highest <= k:
                return True
            return False

        while right < len(s):
            seen[ord(s[right])-65] += 1

            if is_sliding_window_valid():
                longest = max(longest, right - left)
            else: # If sliding window is not valid then shrink it until valid
                while not is_sliding_window_valid():
                    seen[ord(s[left])-65] -= 1
                    left += 1

            right += 1

        return longest + 1
```

Time Complexity O(n)

Space Complexity O(1)

### 567. Permutation in String

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, 
or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1**:

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2**:

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Solution**:

Use a sliding window of size s1 and check if it's the permutation of s1 at each step.

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        right = len(s1) - 1
        frequency_s1 = {}
        frequency_window = {}

        for letter in s1:
            if letter not in frequency_s1:
                frequency_s1[letter] = 1
            else:
                frequency_s1[letter] += 1

        for i in range(right+1):
            if s2[i] not in frequency_window:
                frequency_window[s2[i]] = 1
            else:
                frequency_window[s2[i]] += 1

        while frequency_s1 != frequency_window and right < len(s2) - 1:
            frequency_window[s2[left]] -= 1
            if frequency_window[s2[left]] == 0:
                del frequency_window[s2[left]]
            left += 1
            right += 1
            if s2[right] not in frequency_window:
                frequency_window[s2[right]] = 1
            else:
                frequency_window[s2[right]] += 1

        return frequency_s1 == frequency_window
```

### 76. Minimum Window Substring (Blind)

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the 
**minimum window substring** of s such that every character in `t` (**including 
duplicates**) is included in the window. If there is no such substring, return the 
empty string `""`.

The testcases will be generated such that the answer is **unique**.

A **substring** is a contiguous sequence of characters within the string.

**Example 1**:

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2**:

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3**:

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

**Solution**:

Start from window with size 1
increase the window from right until it includes k
shrink the window from left until it not includes k

save the size of window and left and right somewhere

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) :
            return ""
        window_frequency = {s[0]: 1}
        t_frequency = {}
        s_frequency = {}
        window_left = 0
        window_right = 0
        window_sizes = {}
        min_size = len(s)

        # Calculate s frequency
        for letter in s:
            if letter not in s_frequency:
                s_frequency[letter] = 1
            else:
                s_frequency[letter] += 1

        # Calculate t frequency
        for letter in t:
            if letter not in s_frequency:
                return ""
            if letter not in t_frequency:
                t_frequency[letter] = 1
            else:
                t_frequency[letter] += 1

        def t_in_window():
            for k, v in t_frequency.items():
                if k not in window_frequency or window_frequency[k] < v:
                    return False
            return True

        while True:
            # Increase window from front
            while (not t_in_window()) and (window_right < len(s) - 1):
                window_right += 1

                if s[window_right] not in window_frequency:
                    window_frequency[s[window_right]] = 1
                else:
                    window_frequency[s[window_right]] += 1

            # To get out of infinite loop
            if not t_in_window():
                break

            # Decrease window from back
            while t_in_window():
                window_frequency[s[window_left]] -= 1
                window_left += 1

                window_sizes[window_right - window_left + 2] = [window_left, window_right]
                min_size = min(min_size, window_right - window_left + 2)

        if min_size not in window_sizes:
            return ""
    
        res = ""
        for i in range(window_sizes[min_size][0]-1, window_sizes[min_size][1]+1):
            res += s[i]
        return res
```

Time Complexity: O(n)

Space Complexity: O(n)

### 239. Sliding Window Maximum

You are given an array of integers `nums`, there is a sliding window of 
size `k` which is moving from the very left of the array to the very
right. You can only see the `k` numbers in the window. Each time the 
sliding window moves right by one position.

Return the max sliding window.

**Example 1**:

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2**:

```
Input: nums = [1], k = 1
Output: [1]
```

**Solution**

Use a deque and append the values in it as the window slides
maintain the decreasing order by popping the values from the back if they
are greater than the one you are going to append.

and the window slides check if the number in the front of the deque
is out of window if it is then pop it.

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # Will store numbers in decreasing order
        l = r = 0
        
        while r < len(nums):
            # Pop greater values than current right pointer
            # Before appending to right side
            # To maintain the decreasing ordera
            while len(q) and nums[q[-1]] < nums[r]:
                q.pop()
                
            q.append(r)
            
            # Pop the greatest number or the front number if it's out of window
            if l > q[0]:
                q.popleft()
            
            # Because thre window start with size zero
            # we need to check if the window has grown enough
            # to start sliding the left pointer
            # which we will use to check if the front of the deque
            # is out of window
            if (r + 1 >= k):
                l += 1
                res.append(nums[q[0]])
            
            r += 1
        
        return res
```

Time Complexity: O(n)

Space Complexity: O(n)

## Stack

### 20. Valid Parentheses (Blind)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}
'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example 1**:

```
Input: s = "()"
Output: true
```

**Example 2**:

```
Input: s = "()[]{}"
Output: true
```

**Example 3**:

```
Input: s = "(]"
Output: false
```

**Solution**:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter == "(" or letter == "{" or letter == "[":
                stack.append(letter)
            elif len(stack):
                if letter == ")":
                    if stack[len(stack)-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif letter == "]":
                    if stack[len(stack)-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif letter == "}":
                    if stack[len(stack)-1] == "{":
                        stack.pop()
                    else:
                        return False
            else:
                return False

        return len(stack) == 0
```

Time Complexity: O(n)
Space Complexity: O(n)

### 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum 
element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each 
function.

**Example 1**:

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Solution**:

Use two stack

```python
class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
            
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return []
    
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

### 150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Valid operators are `+`,`-`, `*`, and `/`. Each operand may be an integer or another expression.

**Note** that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


**Example 1**:

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2**:

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3**:

```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

**Solution**:

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        return stack[0]
```

Time Complexity: O(n)
Space Complexity: O(n)

### 22. Generate Parentheses

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1**:

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2**:

```
Input: n = 1
Output: ["()"]
```

**Solution**:

Use recursion and backtracking

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(s, o, c):
            if o == c and c == n:
                res.append(s)

            # If we can open more
            if o < n:
                recurse(s+"(", o+1, c)

            # If we can close
            if c < o:
                recurse(s+")", o, c+1)

        recurse("", 0, 0)

        return res
```

### 739. Daily Temperatures

Given an array of integers `temperatures` represents the daily 
temperatures, return an array `answer`    such that `answer[i]` is the 
number of days you have to wait after the `ith` day to get a warmer 
temperature. If there is no future day for which this is possible, keep 
`answer[i] == 0` instead.

**Example 1**:

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2**:

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3**:

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Solution**:

Use a monotinic decreasing stack

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # Decreasing stack
        
        # Add each value in the stack with index
        for i, v in enumerate(temperatures):
            # If the value we are adding is bigger than the
            # top one then we need to pop the values
            # until to top is not smaller than the one we are 
            # going to add to maintain the decreasing order
            # and as we are popping we can calculate value
            # for the index that we are popping
            while stack and stack[-1][1] < v:
                index, value = stack.pop()
                res[index] = i - index
                
            stack.append([i, v])
        
        return res
```

Time Complexity: O(n)

Space Complexity: O(n)

### 853. Car Fleet

There are `n` cars going to the same destination along a one-lane road. 
The destination is `target` miles away.

You are given two integer array `position` and `speed`, both of length 
`n`, where `position[i]` is the position of the `ith car` and `speed[i]` 
is the speed of the `ith` car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it 
and drive bumper to bumper **at the same speed**. The faster car will 
**slow down** to match the slower car's speed. The distance between these 
two cars is ignored (i.e., they are assumed to have the same position).

A **car fleet** is some non-empty set of cars driving at the same position 
and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will 
still be considered as one car fleet.

Return the **number of car fleets** that will arrive at the destination.


**Example 1**:

```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
```

**Example 2**:

```
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
```

**Example 3**:

```
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
```

**Solution**

Sort the cars by their position (O(n log n)) then scan from right to 
left and keep track of slowest one to arrive at target. If you find
another slower one increase the fleet number.

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        cars = []
        
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        # Sort the cars by position
        cars.sort()
        
        # Calculate time to reach
        def time_to_reach(car):
            return ((target-car[0])/car[1]) # target - position / speed
        
        slowest_car_speed = -1
        fleets = 0
        
        # Find the slowest one to arrive (right to left)
        for car in cars[::-1]:
            if time_to_reach(car) > slowest_car_speed:
                slowest_car_speed = time_to_reach(car)
                fleets += 1
            
        return fleets
```

### 84. Largest Rectangle in Histogram

Given an array of integers `heights` representing the histogram's bar height 
where the width of each bar is `1`, return the area of the largest rectangle 
in the histogram.

***Example 1***:

![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

***Example 2***:

![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

```
Input: heights = [2,4]
Output: 4
```

**Solution**:

[Explaination](https://www.youtube.com/watch?v=zx5Sw9130L0)

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        
        stack = []
        
        for i, v in enumerate(heights):
            start = i
            
            while len(stack) and stack[-1][1] > v:
                index, height = stack.pop()
                largest_area = max(largest_area, height * (i - index))
                start = index
                
            stack.append([start, v])
        
        for i, h in stack:
            largest_area = max(largest_area, h * (len(heights) - i))

        return largest_area
```

## Binary Search

### 704. Binary Search

Given an array of integers `nums` which is sorted in ascending order, and 
an integer `target`, write a function to search `target` in `nums`. If 
`target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1**:

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

**Example 2**:

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

**Solution**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while right >= left:
            mid = (right + left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
```

### 74. Search a 2D Matrix

Write an efficient algorithm that searches for a value `target` in an `m x 
n` integer matrix matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the 
previous row.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

**Solution**:

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        
        def flat_to_mat(i):
            return (i//width, i - ((i//width) * width))
        
        left = 0
        right = (width * height) - 1
        
        while left <= right:
            mid = (left+right) // 2
            x, y = flat_to_mat(mid)
            
            if matrix[x][y] > target:
                right = mid - 1
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                return True
        
        return False
```

Time Comlexity: O(log n)
Space Complexity: O(1)

### 875. Koko Eating Bananas

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile 
has `piles[i]` bananas. The guards have gone and will come back in `h` 
hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she 
chooses some pile of bananas and eats `k` bananas from that pile. If the 
pile has less than `k` bananas, she eats all of them instead and will not 
eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas 
before the guards return.

Return the minimum integer `k` such that she can eat all the bananas 
within `h` hours.

**Example 1**:

```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

**Example 2**:

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

**Example 3**:

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

**Solution**:

The max eating speed is max(piles) and min eating speed is 1.

```python
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        
        def calculate_hour(speed):
            hour = 0
            
            for num in piles:
                hour += ceil(num/speed)
            
            return hour
        
        while left <= right:
            mid = (right+left) // 2

            if calculate_hour(mid) <= h:
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1
        
        return res
```

Time Complexity: O(log max(piles) * piles)

Space Complexity: O(1)

### 33. Search in Rotated Sorted Array (Blind)

There is an integer array `nums` sorted in ascending order (with *distinct* values).

Prior to being passed to your function, `nums` is *possibly rotated* at an unknown 
pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], 
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For 
example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]
`.

Given the array `nums` **after** the possible rotation and an integer `target`, return 
the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1**:

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2**:

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3**:

```
Input: nums = [1], target = 0
Output: -1
```

**Solution**

Just like a normal binary search but with some extra checks

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print(nums[mid])
            
            if nums[mid] == target:
                return mid
            
            # If on the left sorted side
            if nums[0] <= nums[mid]:
                if nums[mid] > target: # If mid is bigger than target
                    if target >= nums[left]: # if the target is in left side
                        right = mid - 1 # Move left side
                    else: # Move right side
                        left = mid + 1
                else: # if mid is smaller than target
                    left = mid + 1
                    
            else: # If on the right sorted side
                if nums[mid] > target: # If mid is bigger than target
                    right = mid - 1
                else: # If mid is smaller than target
                    if nums[right] >= target: # If target on the right side
                        left = mid + 1
                    else: # If target on the left side
                        right = mid - 1
                        
        return -1
                    
```

### 153. Find Minimum in Rotated Sorted Array (Blind)

Suppose an array of length `n` sorted in ascending order is *rotated between* `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of *unique* elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1**:

```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

**Example 2**:

```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

**Example 3**:

```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
```

**Solution**:

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]
        
        while left <= right:
            mid = (right+left) // 2
            res = min(res, nums[mid])
            res = min(res, nums[left])
            res = min(res, nums[right])
            
            if nums[mid] > nums[left] and nums[mid] > nums[right] :
                left = mid + 1
            else:
                right = mid - 1
        
        return res
```

### 981. Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple 
values for the same key at different time stamps and retrieve the key's 
value at a certain timestamp.

Implement the `TimeMap` class:

- `TimeMap()` Initializes the object of the data structure.

- `void set(String key, String value, int timestamp)` Stores the key 
`key` with the value `value` at the given time timestamp.

- `String get(String key, int timestamp)` Returns a value such that `set` 
was called previously, with `timestamp_prev <= timestamp`. If there are 
multiple such values, it returns the value associated with the largest 
`timestamp_prev`. If there are no values, it returns `""`.


**Example 1**:

```
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
```

**Solution**;

```python
class TimeMap:

    def __init__(self):
        self.map = {} # key ->  map 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [[timestamp, value]]
        else:
            self.map[key].append([timestamp, value])
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            print(self.map)
            return ""
        
        values = self.map[key] # timestamp and value
        
        left = 0
        right = len(values) - 1
        mid = 3
        
        while left <= right:
            mid = (left + right) // 2
            
            if values[mid][0] == timestamp:
                return values[mid][1]
            
            if values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        if values[mid][0] > timestamp:
            if mid == 0:
                return ""
            return values[mid-1][1]

        return values[mid][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

### 4. Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` 
respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Example 1**:

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2**:

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Solution**:

https://www.youtube.com/watch?v=q6IEA26hvXc

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        bigger_list = nums1
        smaller_list = nums2
        total_half = (len(nums1) + len(nums2)) // 2
        is_even = (len(bigger_list) + len(smaller_list)) % 2 == 0
        
        # Correct smaller and bigger list
        if len(smaller_list) > len(bigger_list):
            bigger_list, smaller_list = smaller_list, bigger_list
        
        # Binary search for left partition
        left = 0
        right = len(smaller_list) - 1
        
        while True:
            smaller_mid = (left + right) // 2
            bigger_mid = total_half - smaller_mid - 2
            
            smaller_left = smaller_list[smaller_mid] if smaller_mid >= 0 else float("-infinity")
            smaller_right = smaller_list[smaller_mid+1] if (smaller_mid + 1) < len(smaller_list) else float("infinity")
            bigger_left = bigger_list[bigger_mid] if bigger_mid >= 0 else float("-infinity")
            bigger_right = bigger_list[bigger_mid+1] if (bigger_mid + 1) < len(bigger_list) else float("infinity")
            
            if smaller_left <= bigger_right and bigger_left <= smaller_right:
                if is_even:
                    num1 = max(smaller_left, bigger_left)
                    num2 = min(smaller_right, bigger_right)
                    return (num1 + num2) / 2
                else:
                    return min(smaller_right, bigger_right)
            elif smaller_left > bigger_right:
                right = smaller_mid - 1
            else:
                left = smaller_mid + 1
```

Time Complexity: O(log min(num1, num2))


## Linked List

### 206. Reverse Linked List (Blind)

Given the `head` of a singly linked list, reverse the list, and return 
the reversed list.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```
Input: head = [1,2]
Output: [2,1]
```

**Example 3**:

```
Input: head = []
Output: []
```

**Solution**:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev = None
        
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        
        return prev
```

### 21. Merge Two Sorted Lists (Blind)

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2**:

```
Input: list1 = [], list2 = []
Output: []
```

**Example 3**:

```
Input: list1 = [], list2 = [0]
Output: [0]
```

**Solution**:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = None
        head = None
        p1 = list1
        p2 = list2
        
        while p1 or p2:
            new_value = None
            
            if not p1 and p2:
                new_value = p2.val
                p2 = p2.next
            if not p2 and p1:
                new_value = p1.val
                p1 = p1.next
                
            if p1 and p2:
                if p1.val > p2.val:
                    new_value = p2.val
                    p2 = p2.next
                else:
                    new_value = p1.val
                    p1 = p1.next
            
            if not new_node:
                new_node = ListNode(new_value)
                head = new_node
            else:
                new_node.next = ListNode(new_value)
                new_node = new_node.next
        
        return head
```

### 143. Reorder List (Blind)

You are given the head of a singly linked-list. The list can be represented as:

```
L0 ??? L1 ??? ??? ??? Ln - 1 ??? Ln
```

Reorder the list to be on the following form:

```
L0 ??? Ln ??? L1 ??? Ln - 1 ??? L2 ??? Ln - 2 ??? ???
```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

![](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

**Example 2**:

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

**Solution**

Get the middle node

start reversing list from the middle

then merge two nodes.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse half
        current = slow.next
        prev = slow.next = None # To avoid cycle
        
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
            
        # Merge two half
        first, second = head, prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
```

### 19. Remove Nth Node From End of List (Blind)

Given the `head` of a linked list, remove the `nth` node
from the end of the list and return its head.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2**:

```
Input: head = [1], n = 1
Output: []
```

**Example 3**:

```
Input: head = [1,2], n = 1
Output: [1]
```

**Solution**:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = head
        
        # reverse the list
        current = result
        prev = None
            
        while current:
            tmp = current.next;
            current.next = prev
            prev = current
            current = tmp
                
        result = prev
            
        # remove nth node
        count = 1
        prev = None
        current = result
        
        while count < n:
            prev = current
            current = current.next
            count += 1
        
        if prev:
            prev.next = current.next
        else:
            result = current.next
        
        # reverse the list
        current = result
        prev = None
            
        while current:
            tmp = current.next;
            current.next = prev
            prev = current
            current = tmp
                
        result = prev
    
        return result
```

### 138. Copy List with Random Pointer

A linked list of length `n` is given such that each node contains an additional random 
pointer, which could point to any node in the list, or `null`.

Construct a **deep copy** of the list. The deep copy should consist of exactly `n` 
**brand new** nodes, where each new node has its value set to the value of its 
corresponding original node. Both the `next` and `random` pointer of the new nodes 
should point to new nodes in the copied list such that the pointers in the original 
list and copied list represent the same list state. **None of the pointers in the new 
list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random 
--> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random 
--> y`.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of `n` nodes. Each node is 
represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` 
pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.


**Example 1**:

![](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2019/12/18/e2.png)

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

**Example 3**:

![](https://assets.leetcode.com/uploads/2019/12/18/e3.png)

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

**Solution**:

Use a hashmap

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newNodes = { None : None }
        current = head
        
        while current:
            newNodes[current] = Node(current.val)
            current = current.next
            
        current = head
        
        while current:
            newNodes[current].next = newNodes[current.next]
            newNodes[current].random = newNodes[current.random]
            current = current.next
            
        return newNodes[head]
```

### 2. Add Two Numbers

You are given two **non-empty** linked lists representing two 
non-negative integers. The digits are stored in **reverse 
order**, and each of their nodes contains a single digit. Add 
the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading 
zero, except the number 0 itself.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2**:

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3**:

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

**Solution**:

Converting linked list to number is easy: 1st * 1 + 2nd * 10 + 3rd * 100 + ...

Then convert the final number to string to linked list

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        place = 1
        l1_num = 0
        
        while current:
            l1_num += current.val * place
            place *= 10
            current = current.next
        
        current = l2
        place = 1
        l2_num = 0
        
        while current:
            l2_num += current.val * place
            place *= 10
            current = current.next
            
        res_num = str(l1_num + l2_num)

        res = ListNode()
        cur = None
        
        for val in reversed(res_num):
            if cur == None:
                cur = ListNode(val)
                res = cur
            else:
                cur.next = ListNode(val)
                cur = cur.next
        
        return res
```

### 141. Linked List Cycle (Blind)

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Example 1**:

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3**:

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

**Solution**:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}

        current = head
        
        while current:
            if current in seen:
                return True
            else:
                seen[current] = True
            current = current.next
            
        return False
```

### 287. Find the Duplicate Number

Given an array of integers `nums` containing `n + 1` integers 
where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return this 
repeated number.

You must solve the problem **without** modifying the array `nums` 
and uses only constant extra space.

**Example 1**:

```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2**:

```
Input: nums = [3,1,3,4,2]
Output: 3
```

**Solution**:

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
                
        slow2 = 0
        
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                break
                
        return slow
```

### 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with 
**positive** size `capacity`.

- `int get(int key)` Return the value of the `key` if the key 
exists, otherwise return `-1`.

- `void put(int key, int value)` Update the value of the `key` if 
the key exists. Otherwise, add the `key-value` pair to the cache. If 
the number of keys exceeds the `capacity` from this operation, 
**evict** the least recently used key.

- The functions `get` and `put` must each run in `O(1)` average time complexity.


**Example 1**:

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

**Solution**:

Use a doubly linked list where the left side is the least used
and the right side is most used and store the pointer to the node
in linked list in a hashmap.

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.least, self.most = Node(0, 0), Node(0, 0)
        self.least.next, self.most.prev = self.most, self.least

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    # Insert from most
    def insert(self, node):
        prev = self.most.prev
        prev.next = node
        node.prev = prev
        node.next = self.most
        self.most.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # Update if exists
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].value = value
        else: # If key doesn't exist
            if len(self.cache) >= self.capacity: # If we are out of capacity
                least_used = self.least.next
                del self.cache[least_used.key]
                self.remove(least_used)
            # Insert new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

### 23. Merge k Sorted Lists (Blind)

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it*.

**Example 1**:

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

**Example 2**:

```
Input: lists = []
Output: []
```

**Example 3**:

```
Input: lists = [[]]
Output: []
```

**Solution**:

Use divide and conquer method

![](https://leetcode.com/problems/merge-k-sorted-lists/Figures/23/23_divide_and_conquer_new.png)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        
        return lists[0]
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = None
        head = None
        p1 = list1
        p2 = list2
        
        while p1 or p2:
            new_value = None
            
            if not p1 and p2:
                new_value = p2.val
                p2 = p2.next
            if not p2 and p1:
                new_value = p1.val
                p1 = p1.next
                
            if p1 and p2:
                if p1.val > p2.val:
                    new_value = p2.val
                    p2 = p2.next
                else:
                    new_value = p1.val
                    p1 = p1.next
            
            if not new_node:
                new_node = ListNode(new_value)
                head = new_node
            else:
                new_node.next = ListNode(new_value)
                new_node = new_node.next
        
        return head
```

Time Complexity: O(n log k) where k is number of linked list and n
is total number of nodes in two lists.

Space Complexity: O(1)

### 25. Reverse Nodes in k-Group

Given the `head` of a linked list, reverse the nodes of the list `k` at a 
time, and return the modified *list*.

`k` is a positive integer and is less than or equal to the length of the 
linked list. If the number of nodes is not a multiple of `k` then left-out 
nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves 
may be changed.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Solution**:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = []
        groups = []
        
        current = head
        
        while current:
            tmp.append(current.val)
            
            if len(tmp) == k:
                groups.append(tmp)
                tmp = []
        
            current = current.next
        
        groups.append(tmp)

        new_list = ListNode(0)
        new_head = new_list
        
        for group in groups:
            if len(group) == k:
                group = reversed(group)
                
            for num in group:
                new_list.next = ListNode(num)
                new_list = new_list.next
                
        return new_head.next
```

### Trees

#### 226. Invert Binary Tree (Blind)

Given the `root` of a binary tree, invert the tree, and return its *root*.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```
Input: root = [2,1,3]
Output: [2,3,1]
```

**Example 3**:

```
Input: root = []
Output: []
```

**Solution**:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

### 104. Maximum Depth of Binary Tree (Blind)

Given the `root` of a binary tree, return *its maximum depth*.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2**:

```
Input: root = [1,null,2]
Output: 2
```

**Solution**:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

### 543. Diameter of Binary Tree

Given the `root` of a binary tree, return the length of the **diameter** of 
the tree.

The **diameter** of a binary tree is the **length** of the longest path 
between any two nodes in a tree. This path may or may not pass through the 
`root`.

The **length** of a path between two nodes is represented by the number of 
edges between them.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2**:

```
Input: root = [1,2]
Output: 1
```

**Solution**:

Count the left and right height for each nodes add them together and the highest diameter (left height + right height + 1) is the answer.


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        self.cache = {} # For memoization
        
        self.max_diameter = 0
        
        self.depthOfBinaryTree(root)
        
        return self.max_diameter - 1
        
    def depthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root in self.cache:
            return self.cache[root]
        
        if root == None:
            self.cache[root] = 0
            return 0
        
        lh = self.depthOfBinaryTree(root.left)
        rh = self.depthOfBinaryTree(root.right)
        
        self.max_diameter = max(self.max_diameter, lh+rh+1)
        
        h = max(lh, rh) + 1
        self.cache[root] = h
        
        return h

```

### 110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

>a binary tree in which the left and right subtrees of every node differ in 
>height by no more than 1.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3**:

```
Input: root = []
Output: true
```

**Solution**:

Use dfs and check the lowest one first 

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root: Optional[TreeNode]) -> [bool, int]:
            if not root:
                return [True, 0]
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            balanced = (l[0] and r[0] and 
                        abs(l[1] - r[1]) <= 1)
            
            return [balanced, max(l[1], r[1]) + 1]
        
        return dfs(root)[0]
```

### 100. Same Tree (Blind)

Given the roots of two binary trees `p` and `q`, write a function to check if 
they are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3**:

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

**Solution**:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        
        if not (p and q):
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### 572. Subtree of Another Tree (Blind)

Given the roots of two binary trees `root` and `subRoot`, 
return `true` if there is a subtree of `root` with the same 
structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of 
a node in `tree` and all of this node's descendants. The 
tree `tree` could also be considered as a subtree of itself.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)

```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)

```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

**Solution**:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        
        if not (root and subRoot):
            return False
        
        return ((self.isSubtree(root.left, subRoot)) or 
                (self.isSubtree(root.right, subRoot)) or
                (self.isSameTree(root, subRoot)))
    
    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 == None and tree2 == None:
            return True
        
        if not (tree1 and tree2):
            return False
        
        return ((tree1.val == tree2.val) and
                (self.isSameTree(tree1.left, tree2.left)) and 
                (self.isSameTree(tree1.right, tree2.right)))
```

### 235. Lowest Common Ancestor of a Binary Search Tree (Blind)

Given a binary search tree (BST), find the lowest common 
ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest 
common ancestor is defined between two nodes `p` and `q` as 
the lowest node in `T` that has both `p` and `q` as 
descendants (where we allow **a node to be a descendant of 
itself**)."

**Example 1**:

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

**Example 3**:

```
Input: root = [2,1], p = 2, q = 1
Output: 2
```

### 102. Binary Tree Level Order Traversal (Blind)

Given the `root` of a binary tree, return *the level order 
traversal of its nodes' values*. (i.e., from left to right, 
level by level).

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2**:

```
Input: root = [1]
Output: [[1]]
```

**Example 3**:

```
Input: root = []
Output: []
```

**Solution**:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return  []
        
        current_level = [root]
        res = []
        
        while current_level:
            res.append([node.val for node in current_level])
            new_level = []
            for node in current_level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            current_level = new_level
            
        return res
```

### 199. Binary Tree Right Side View

Given the `root` of a binary tree, imagine yourself standing on the *right side* of it, return the values of the nodes you can see ordered from top to bottom.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/02/14/tree.jpg)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Example 2**:

```
Input: root = [1,null,3]
Output: [1,3]
```

**Example 3**:

```
Input: root = []
Output: []
```

**Solution**:

Use BFS

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return  []
        
        current_level = [root]
        res = []
        
        while current_level:
            res.append(current_level[-1].val)
            
            new_level = []
            
            for node in current_level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
                
            current_level = new_level
            
        return res
```

### 1448. Count Good Nodes in Binary Tree

Given a binary tree `root`, a node X in the tree is named 
**good** if in the path from root to X there are no nodes 
with a value greater than X.

Return the number of **good** nodes in the binary tree.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png)

```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```


**Example 2**:

![](https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png)

```
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```

**Example 3**:

```
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
```

**Solution**:

Use dfs and keep track of greatest seen number

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, greatest):
            if not node:
                return 0
            
            count = 0
            
            if node.val >= greatest:
                count = 1
                
            return count + dfs(node.left, max(node.val, greatest)) + dfs(node.right, max(node.val, greatest))
        
        return dfs(root, root.val)
```

### 98. Validate Binary Search Tree (Blind)

Given the `root` of a binary tree, determine if it is a valid binary search tree 
(BST).

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's 
key.
- The right subtree of a node contains only nodes with keys **greater than** the 
node's key.

- Both the left and right subtrees must also be binary search trees.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

```
Input: root = [2,1,3]
Output: true
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

**Solution**:

Use dfs and keep track of high limit and low limit starting at inf and -inf

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low=-math.inf, high=math.inf) -> bool:
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root)
```

### 230. Kth Smallest Element in a BST (Blind)

Given the `root` of a binary search tree, and an integer `k`, 
return the `kth` smallest value (**1-indexed**) of all the 
values of the nodes in the tree.


**Example 1**:

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

**Solution**:

Use inorder traversal (preferably using iteration)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            
            k -= 1
            
            if not k:
                return root.val
            root = root.right
```

Time Complexity: O(H+K) where H is the height of the tree

Space Complexity: O(H)

### 105. Construct Binary Tree from Preorder and Inorder Traversal (Blind)

Given two integer arrays `preorder` and `inorder` where 
`preorder` is the preorder traversal of a binary tree and 
`inorder` is the inorder traversal of the same tree, 
construct and return the *binary tree*.

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2**:

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

**Solution**

The first element of the preorder is the root node
and we can know which ones will go to left and right by 

finding the number in the inorder list, all the numbers on 
the left side will go in left side of the tree and all the 
numbers on the right side will go right side of the tree

if `mid` is the index of the root node in inorder
then the ``1 to `mid + 1` **(exclusive)** of preorder and 
`0` to `mid` **(exclusive)** of inorder will go to left 
and `mid + 1` to last of preorder and inorder will go to 
right

Do this recursively

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
```

### 124. Binary Tree Maximum Path Sum (Blind)

A **path**   in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum **path sum** of any **non-empty** path.


**Example 1**:

![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

**Solution**:

Use dfs calculate the max sum of lower nodes first then upper

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            
            total = left + right + root.val
            
            res = max(res, total)
            
            return max(left, right) + root.val
        
        dfs(root)
        return res
```

### 297. Serialize and Deserialize Binary Tree (Blind)

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

**Example 2**:

```
Input: root = []
Output: []
```

**Solution**:

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        def dfs(node) -> str:
            if not node:
                return "n"
            
            s = str(node.val) + ","
            
            s += dfs(node.left) + ","
            s += dfs(node.right)
            
            return s
    
        return dfs(root)
    
    def deserialize(self, data):
        l = data.split(",")
        
        i = 0
        
        def dfs():
            nonlocal i
            
            if l[i] == "n":
                i += 1
                return None
            
            node = TreeNode(int(l[i]))
            
            i += 1
            
            node.left = dfs()
            node.right = dfs()
        
            return node
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
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

### 211. Design Add and Search Words Data Structure (Blind)

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure 
that matches `word` or `false` otherwise. `word` may contain   
dots `'.'` where dots can be matched with any letter.

**Example***:

```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

**Solution**:

```python
class Node:
    def __init__(self, value, end):
        self.value = value
        self.nexts = {}
        self.end = end

class WordDictionary:

    def __init__(self):
        self.root = Node(None, False)

    def addWord(self, word: str) -> None:
        current = self.root
        
        for i, letter in enumerate(word):
            if letter not in current.nexts:
                current.nexts[letter] = Node(letter, False)
                
            if i == len(word)-1:
                current.nexts[letter].end = True
            else:
                current = current.nexts[letter]
            

    def search(self, word: str) -> bool:
        
        def dfs(node, pointer) -> bool:
            if pointer >= len(word):
                return False
            
            letter = word[pointer]
            
            if letter != ".":
                if letter in node.nexts:
                    if pointer == len(word) - 1 and node.nexts[letter].end:
                        return True
                    return dfs(node.nexts[word[pointer]], pointer+1)
                else:
                    return False
            else:
                if not len(node.nexts):
                    return False
                
                for k in node.nexts:
                    if pointer == len(word) - 1 and node.nexts[k].end:
                        return True
                    
                    if dfs(node.nexts[k], pointer+1):
                        return True
                
                return False
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

### 212. Word Search II (Blind)

Given an `m x n` board of characters and a list of strings 
words, return all `words` on the board.

Each word must be constructed from letters of sequentially 
**adjacent cells**, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be used 
more than once in a word.

**Example 1**:

![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Example 2**:

![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)

```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

**Solution**:

Store all the words in a trie then use dfs on the trie and
the board and remove the word from the trie as you find them

```python
class TreeNode:
    def __init__(self):
        self.nexts = {}
        self.end = False
        
    def add_word(self, word):
        current = self
        for letter in word:
            if letter not in current.nexts:
                current.nexts[letter] = TreeNode()
            current = current.nexts[letter]
        current.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TreeNode()
        
        # Store all words in trie
        for word in words:
            root.add_word(word)
            
        rows, cols = len(board), len(board[0])
        
        res = []
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
               r == rows or c == cols or
               board[r][c] == None or board[r][c] not in node.nexts):
                return
            
            prev = node
            l = board[r][c]
            node = node.nexts[l]
            word += l
            
            if node.end:
                # Remove word from trie
                node.end = False
                if len(node.nexts) == 0:
                    del prev.nexts[l]
                    
                res.append(word)
            
            board[r][c] = None
            
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            
            board[r][c] = l
            
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
                
        return res
```

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

### 973. K Closest Points to Origin

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., `???(x1 - x2)2 + (y1 - y2)2`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

**Example 1**:

![](https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg)

```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

**Example 2**:

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

**Solution**:

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2) # using this formula increases performance
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res
```

### 215. Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

You must solve it in `O(n)` time complexity.

**Example 1**:

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2**:

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Solution**:

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            if len(heap) == k+1:
                heapq.heappop(heap)
                
            heapq.heappush(heap, num)
        
        k_nums = []
        
        while heap:
            k_nums.append(heapq.heappop(heap))
 
        return k_nums[-k]
```

n log k is pretty close to n if k is small

### 621. Task Scheduler

Given a characters array `tasks`, representing the tasks a CPU needs to do, 
where each letter represents a different task. Tasks could be done in any 
order. Each task is done in one unit of time. For each unit of time, the CPU 
could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown 
period between two **same tasks** (the same letter in the array), that is 
that there must be at least `n` units of time between any two same tasks.

Return *the least number of units of times that the CPU will take to finish 
all the given tasks*.

**Example 1**:

```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```

**Example 2**:

```
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
```

**Example 3**:

```
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
```

**Solution**

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # length of maximum occuring character
        maxTaskCount = max(Counter(tasks).values())
        # total number of characters occuring at max times
        maxCountRepeats = Counter(Counter(tasks).values())[maxTaskCount]

        return max(len(tasks), ((maxTaskCount-1) * (n+1)) + maxCountRepeats)
        
```

**maxTaskCount** = length of maximum occuring character
**maxCountRepeats** = total number of character that are occuring for max times.

Let's take a example **AAABBBC** , **n=2**
maxTaskCount: 3 => `AAA` and `BBB`
maxCountRepeats: 2 => `AAA` and `BBB`
result: 7 => `ABCAB#AB`

First we try to fill most frequent character and a empty gap of length `n` is created between these two characters.

`A _ _ A _ _ A`

Here places of most frequent character is fixed, and in empty spaces we have to fill remaining character, we can also notice that length of all part (excluding last character `'A'`) is equals to `(maxTaskCount - 1) * (n+1)` , i.e. `A _ _ A _ _`.

Reason: As we are excluding last `'A'` total slots created is `(maxTaskCount-1)` and after including `'A'` and empty spaces `(A _ _ )`, length of one slot is `(n+1)`
so, length after excluding last `'A'` = `(maxTaskCount-1)*(n+1)`.

But, there can be a case where more than one character can appear for max times, so in this case we have to fill second character just after first,

`A B _ A B _ A B`

in this case, length of last part which was excluded earlier is equals to `maxCountRepeats`, `A B _ A B _ A B`
so, `totalLength = ((maxTaskCount-1) * (n+1)) + maxCountRepeats`

But, wait!, what if we have given n=0, we don't have to bother about the order of occurences, so it result will be equals to tasks.length.
So,

`result = max(len(tasks), ((maxTaskCount-1) * (n+1)) + maxCountRepeats)`

### 355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed.

Implement the `Twitter` class:

- `Twitter()` Initializes your twitter object.
- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID `tweetId` by the user 
`userId`. Each call to this function will be made with a unique `tweetId`.
- `List<Integer> getNewsFeed(int userId)` Retrieves the `10` most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be **ordered from most recent to least recent**.
- `void follow(int followerId, int followeeId)` The user with ID `followerId` started following the user with ID `followeeId`.
- `void unfollow(int followerId, int followeeId)` The user with ID `followerId` started unfollowing the user with ID `followeeId`.

**Example 1**:

```
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
```

**Solution**:

```python
class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1
        
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        
        if userId not in self.follows:
            self.follows[userId] = set()
        
        self.follows[userId].add(userId)
        
        for user in self.follows[userId]:
            if user in self.tweets:
                index = len(self.tweets[user]) - 1
                count, tweetId = self.tweets[user][index]
                
                heap.append([count, tweetId, user, index-1])
                
        heapq.heapify(heap)
        
        while heap and len(res) < 10:
            count, tweetId, user, index = heapq.heappop(heap)
            res.append(tweetId)
            
            if index >= 0:
                count, tweetId = self.tweets[user][index]
                heapq.heappush(heap, [count, tweetId, user, index-1])
        
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

### 295. Find Median from Data Stream (Blind)

The *median* is the middle value in an ordered integer list. If the size of 
the list is even, there is no middle value and the median is the mean of the 
two middle values.

For example, for `arr = [2,3,4]`, the median is 3``.
For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

**Example 1**:

```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

**Solution**:

Slit the storted stream into two parts `left` and `right` using max-heap
for `left` and min-heap for `right` and make sure the length of `left` is almost equal to length of `right`.

```python
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
```

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

```python
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
### 78. Subsets

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1**:

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2**:

```
Input: nums = [0]
Output: [[],[0]]
```

**Solution**:

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        
        return res
```