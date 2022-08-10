# Add Two Numbers

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