# Reverse Nodes in k-Group

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