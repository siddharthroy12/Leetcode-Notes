# Remove Nth Node From End of List (Blind)

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