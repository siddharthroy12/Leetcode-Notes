# Reverse Linked List (Blind)

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