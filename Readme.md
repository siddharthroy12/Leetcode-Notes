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
6. [Trie](#trie)
    1. [Implement Trie (Blind)](#208-implement-trie-blind)
7. [Heap and Priority Queue](#heap-and-priority-queue)
    1. [Kth Largest Element in a Stream](#703-kth-largest-element-in-a-stream)
    2. [Last Stone Weight](#1046-last-stone-weight)
8. [Backtracking](#backtracking)
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
