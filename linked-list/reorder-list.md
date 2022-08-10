# Reorder List

You are given the head of a singly linked-list. The list can be represented as:

```
L0 → L1 → … → Ln - 1 → Ln
```

Reorder the list to be on the following form:

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
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
